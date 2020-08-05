from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def index(request):
    return HttpResponse("Placeholder to later list all blogs")

def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog")

# This is just a redirection
def create(request):
    print("you created a new blog post dude")
    return redirect('/')
    
def show(request,number):
    return HttpResponse(f"This is a placeholder to display blog number {number} ")

def edit(request,number):
    return HttpResponse(f"This is a placeholder to edit blog number {number}")

def destroy(request,number):
    print(f"you totally destroyed blog number {number}")
    return redirect('/')