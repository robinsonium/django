from django.shortcuts import render, HttpResponse, redirect
from courses_app.models import Course, Description

# Create your views here.
def index(request):
    
    context={
        "courses":Course.objects.all(),
    }
    print("context:",context)
    return render(request,"index.html",context)

def new(request):
    # receive form data and update DB
    print(request.POST)
    this_description=Description.objects.create(content=request.POST['course_description'])
    Course.objects.create(name=request.POST['course_name'],description=this_description)
    return redirect('courses')
    

def destroy(request,id):
    return HttpResponse("placeholder for views.destroy")