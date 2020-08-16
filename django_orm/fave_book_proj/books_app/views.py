from django.shortcuts import render, redirect, HttpResponse
from login_app.models import User
from books_app.models import Book

# Create your views here.

def books(request):
    context={
        "books":Book.objects.all(),
        "user":User.objects.get(id=request.session['userid']),
    }
    return render(request,"welcome.html",context)

def add_book(request):
    title=request.POST['title']
    description=request.POST['description']
    user=User.objects.get(id=request.session['userid'])
    this_book=Book.objects.create(title=title, description=description,uploaded_by=user)
    this_book.users_who_like.add(user)
    return redirect('/books')

def details(request,id):
    context={
        "book":Book.objects.get(id=id),
        "user":User.objects.get(id=request.session['userid']),
    }
    return render(request,"detail.html",context)

# favorite a book
def like(request,id):
    this_book=Book.objects.get(id=id)
    this_user=request.session['userid']
    this_book.users_who_like.add(this_user)
    this_book.save()
    return redirect('/books')

# edit a book, if logged in user uploaded it
def edit(request,id):
    title=request.POST['title']
    description=request.POST['description']
    this_book=Book.objects.get(id=id)
    this_book.title=title
    this_book.description=description
    this_book.save()
    return redirect('/books')

# delete a book, if logged in user deleted it
def delete(request,id):
    this_book=Book.objects.get(id=id)
    this_book.delete()
    return redirect('/books')

def logout(request):
    request.session.flush()
    return redirect('/')