from django.shortcuts import render, redirect, HttpResponse
from message_app.models import Message
from login_app.models import User

# Create your views here.
def show_wall(request):
    print("just got called to show the wall")
    context={
        "messages":Message.objects.all(),
    }
    return render(request,"thewall.html",context)

def add_message(request):
    if request.method=="POST":
        # print("adding message to database, proceeding to redirect")
        user=User.objects.get(id=request.session['userid'])
        Message.objects.create(content=request.POST['message'],poster=user)
    return redirect('./show_wall')

def add_comment(request):
    return HttpResponse("Placeholder for add_comment")

def delete_comment(request):
    return HttpResponse("placeholder for delete_comment()")    