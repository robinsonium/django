from django.shortcuts import render, HttpResponse, redirect
from .models import User

# Create your views here.
def index(request):
    context={
        "all_users":User.objects.all()
    }
    # foo=User.objects.all()
    # for user in foo:
    #     print(user.first_name)
    return render(request,"index.html",context)

def add_user(request):
    fname=request.POST['first_name']
    lname=request.POST['last_name']
    email=request.POST['email_address']
    age=request.POST['age']
    new_user=User(first_name=fname,last_name=lname,email_address=email,age=age)
    new_user.save()
    return redirect("/")