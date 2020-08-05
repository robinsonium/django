from django.shortcuts import render, HttpResponse, redirect
from shows_app.models import Show
from django.contrib import messages
from datetime import datetime

# Create your views here.
def shows(request):
        context={
            "shows":Show.objects.all()
        }
        return render(request,"shows.html",context)
    

def new(request):
    if request.method=="POST":
        errors = Show.objects.validate_show(request.POST)
        if len(errors) > 0:
            for value in errors.values():
                messages.error(request, value)
            return redirect('/shows/new')
        
        title=request.POST['title']
        network=request.POST['network']
        release_date=request.POST['release_date']
        description=request.POST['description']
        this_show=Show.objects.create(title=title,network=network,release_date=release_date,description=description)
        show_id=this_show.id
        return redirect(f"/details/{show_id}")
    return render(request,"new.html")

def details(request,show_id):
        this_show=Show.objects.get(id=show_id)
        context={
            "show":this_show
        }
        return render(request,"details.html",context)

def edit(request,show_id):
    this_show=Show.objects.get(id=show_id)
    context={
        "show":this_show,
        "release_date":this_show.release_date
    }
    if request.method=="GET":
        return render(request,'edit.html',context)
    #else if POST,
    errors = Show.objects.validate_show(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect(f'/details/{show_id}/edit')
    this_show.title=request.POST['title']
    this_show.network=request.POST['network']
    this_show.release_date=request.POST['release_date']
    this_show.description=request.POST['description']
    this_show.save()
    return redirect(f"/details/{show_id}")

def destroy(request,show_id):
    this_show=Show.objects.get(id=show_id)
    print("this_show:",this_show)
    this_show.delete()
    return redirect('/shows')

def index(request):
    return redirect('/shows')


## backup code
# def new(request):
#     if request.method=="POST":
#         errors = Show.objects.validate_show(request.POST)
#         if len(errors) > 0:
#             print("we had errors")
#             for key, value in errors.items():
#                 messages.error(request, value)
#         return redirect('new')
#     else:
#         title=request.POST['title']
#         network=request.POST['network']
#         release_date=request.POST['release_date']
#         description=request.POST['description']
#         this_show=Show.objects.create(title=title,network=network,release_date=release_date,description=description)
#         show_id=this_show.id
#         return redirect(f"/details/{show_id}")
#     return render(request,"new.html")