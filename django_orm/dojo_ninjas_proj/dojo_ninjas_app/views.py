from django.shortcuts import render, HttpResponse, redirect
from .models import Dojo,Ninja

# Create your views here.
def index(request):
    context={
        "all_dojos":Dojo.objects.all()
    }
    return render(request,'index.html',context)

def add_dojo(request):
    # return HttpResponse("placeholder for add_dojo()")
    name=request.POST['name']
    city=request.POST['city']
    state=request.POST['state']
    Dojo.objects.create(name=name,city=city,state=state)
    return redirect('/')

def add_ninja(request):
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    dojo=Dojo.objects.get(id=request.POST['dojo'])
    Ninja.objects.create(first_name=first_name,last_name=last_name,dojo=dojo)
    return redirect('/')

def delete_dojo(request):
    dojo=Dojo.objects.get(id=request.POST['dojo'])
    dojo.delete()
    return redirect('/')

