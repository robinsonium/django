from django.shortcuts import render, redirect, HttpResponse
import bcrypt

# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    pass

def registration(request):
    if request.method == "POST":
        

def success(request):
    pass