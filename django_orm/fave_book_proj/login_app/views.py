from django.shortcuts import render, redirect, HttpResponse
import bcrypt
from login_app.models import *
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, "index.html")


def login(request):
    if request.method=="GET":
        return redirect('/')
    this_user = User.objects.filter(email=request.POST['email'])
    if this_user:
        logged_user = this_user[0]
        if bcrypt.checkpw(request.POST['password'].encode('utf8'), logged_user.password.encode('utf8')):
            print('successful login')
            request.session['userid'] = logged_user.id
            request.session['email'] = logged_user.email
    return redirect('/success')


def registration(request):
    if request.method == "POST":
        errors = User.objects.validate(request.POST)
        if len(errors) > 0:
            for value in errors.values():
                messages.error(request, value)
            return redirect('/')
    pw = request.POST['password']  # helper variable to keep things readable
    pw_hash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt()).decode()
    this_user = User.objects.create(first_name=request.POST['first_name'],
                                    last_name=request.POST['last_name'],
                                    email=request.POST['email'],
                                    birthday=request.POST['birthday'],
                                    password=pw_hash)
    request.session['userid']=this_user.id
    return redirect('/success')


def success(request):
    if 'userid' in request.session:#.keys():
        this_user = User.objects.get(id=request.session['userid'])
        request.session['first_name'] = this_user.first_name
        print("user is in session")
        return render(request, "success.html")
    else:
        return redirect('/')


def logout(request):
    print(request.session['userid'])
    request.session.flush()
    return redirect('/')
