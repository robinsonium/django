from django.shortcuts import render, redirect, HttpResponse
import bcrypt
from django.contrib import messages
from quotes_app.models import *

# Create your views here.
def index(request):
    print("reached index.html")
    return render(request,"index.html")

def register(request):
    if request.method=="POST":
        print("reached views.register, attempting to validate")
        errors = User.objects.validate_reg(request.POST)
        if errors:
            for value in errors.values():
                messages.error(request, value)
            return redirect('/')
        print("reached validation")
        f_name=request.POST['first_name']
        l_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()).decode()
        this_user=User.objects.create(
            first_name=f_name,
            last_name=l_name,
            email=email,
            password=pw_hash
        )
        #Using this as a unique lookup instead of ID, so that we can filter for the correct user later
        request.session['email']=this_user.email 
        print("sucessful registration, attempting redirect to success")
        return redirect('/success')
    return redirect('/')

def login(request):
    if request.method=='POST':
        print("starting login")
        errors = User.objects.validate_login(request.POST)
        if errors:
            print("validation errors occurred")
            for value in errors.values():
                messages.error(request, value)
            return redirect('/')
        this_user = User.objects.filter(email=request.POST['email'])
        if this_user:
            this_user = this_user[0]
            if bcrypt.checkpw(request.POST['password'].encode('utf8'), this_user.password.encode('utf8')):
                request.session['email'] = this_user.email
                request.session['userid'] = this_user.id
                print("successful login")
                return redirect('/success')
            errors['password']="Incorrect password"
            for value in errors.values():
                messages.error(request, value)
            return redirect('/')
    return(redirect('/'))


def success(request):
    print("reached views.success")
    this_user=User.objects.filter(email=request.session['email'])
    this_user=this_user[0]
    context={
        "user":this_user
    }
    return render(request,"success.html",context)

def logout(request):
    request.session.flush()
    return redirect('/')

def quotes(request):
    # context needs to include the logged in user and all quotes
    this_user=User.objects.filter(email=request.session['email'])
    this_user=this_user[0]
    context={
        "user":this_user,
        "quotes":Quote.objects.all(),

    }
    return render(request,"dashboard.html",context)

def add_quote(request):
    if request.method=="POST":
        errors = Quote.objects.validate(request.POST)
        if errors:
            for value in errors.values():
                messages.error(request, value)
            return redirect('/quotes')
        this_user=User.objects.filter(email=request.session['email'])
        this_user=this_user[0]
        print("this_user",this_user)
        content=request.POST['content']
        author=request.POST['author']
        Quote.objects.create(author=author, content=content, posted_by=this_user)
        return redirect('/quotes')

def view_profile(request,id):
    logged_user=User.objects.get(id=id)
    context={
        "user":logged_user
    }
    return render(request,"profile.html",context)

def delete(request,id):
    this_quote=Quote.objects.get(id=id)
    this_quote.delete()
    return redirect('/quotes')

def like(request,id):
    this_quote=Quote.objects.get(id=id)
    logged_user=User.objects.get(id=request.session['userid'])
    this_quote.likes.add(logged_user)
    this_quote.save()
    return redirect('/quotes')


def edit(request,id):
    this_user=User.objects.get(id=id)
    if request.method == "POST":
        errors = User.objects.validate_edit(request.POST)
        if errors:
            for value in errors.values():
                messages.error(request, value)
            return redirect(f'/edit/{this_user.id}')
        this_user.first_name=request.POST['first_name']
        this_user.last_name=request.POST['last_name']
        this_user.email=request.POST['email']
        this_user.save()
        # In case we updated email, make sure the proper value is in session
        request.session['email']=this_user.email
        return redirect('/quotes')
    context={
        "user":this_user,
    }
    return render(request,"edit.html",context)

