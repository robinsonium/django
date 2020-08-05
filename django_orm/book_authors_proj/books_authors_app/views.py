from django.shortcuts import render, redirect, HttpResponse
from books_authors_app.models import *

# Create your views here.


def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'index.html', context)


def add_book(request):
    # if request.method=="post":
    title = request.POST['title']
    desc = request.POST['desc']
    Book.objects.create(title=title, desc=desc)
    print("books: ", Book.objects.all())
    context = {
        'books': Book.objects.all()
    }
    return render(request, "index.html", context)


def view_book(request, id):
    this_book=Book.objects.get(id=id)
    my_authors=[author for author in Author.objects.all() if author not in this_book.authors.all()]
    context = {
        "book": this_book,
        "authors": my_authors,
    }
    return render(request, "view_book.html", context)

def author_details(request,id):
    this_author=Author.objects.get(id=id)
    # get a list of books that are not already associated with this author
    my_books=[book for book in Book.objects.all() if book not in this_author.books.all()]
    context={
        "all_books":my_books,
        "author":this_author,
    }
    print("this author",this_author)
    print("my books",my_books)

    # context={
    #     "author":Author.objects.get(id=id),
    #     "all_books":Book.objects.all(),
    # }
    return render(request,"author_detail.html",context)

def view_authors(request):
    context = {
        "authors": Author.objects.all(),
    }
    return render(request, "authors.html", context)


def add_author(request, book_id):
    auth_id = request.POST['auth']
    book_id = book_id
    this_book = Book.objects.get(id=book_id)
    this_author = Author.objects.get(id=auth_id)
    this_book.authors.add(this_author)
    this_book.save()
    return redirect('/')


def create_author(request):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    Author.objects.create(first_name=first_name, last_name=last_name)
    return redirect('/view_authors')

def delete_author(request):
    auth_id=request.POST['auth_id']
    author=Author.objects.get(id=auth_id)
    author.delete()
    return redirect('/view_authors')

def add_book_to_author(request, auth_id):
    this_author=Author.objects.get(id=auth_id)
    book_id=request.POST['book']
    this_book=Book.objects.get(id=book_id)
    this_author.books.add(this_book)
    return redirect('/view_authors')

def edit_book(request):
    pass