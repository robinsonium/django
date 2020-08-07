from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from courses_app.models import Course, Description, Comment

# Create your views here.
def index(request):
    context={
        "courses":Course.objects.all(),
    }
    print("context:",context)
    return render(request,"index.html",context)

def new(request):
    if request.method=="POST":
        errors = Course.objects.validate(request.POST)
        if len(errors) > 0:
            for value in errors.values():
                messages.error(request, value)
        return redirect('/')
    this_description=Description.objects.create(content=request.POST['course_description'])
    Course.objects.create(name=request.POST['course_name'],description=this_description)
    print("added course!")
    return redirect('/')

def prompt(request,id):
    context={
        "course":Course.objects.get(id=id),
    }
    return render(request,"delete.html",context)
    

def destroy(request,id):
    this_course=Course.objects.get(id=id)
    this_course.delete()
    return redirect('/courses')

def comment(request,id):
    context={
        "course":Course.objects.get(id=id)
    }
    
    return render(request,"comment.html",context)

def add_comment(request,id):
    if request.method=="POST":
        comment=request.POST['comment']
        this_course=Course.objects.get(id=id)
        Comment.objects.create(content=comment,course=this_course)
    return redirect('/')
    