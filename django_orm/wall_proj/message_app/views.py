from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
import pytz
import re
from pytz import timezone
from dateutil.relativedelta import relativedelta
from message_app.models import Message, Comment
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
    if request.method=="POST":
        user=User.objects.get(id=request.session['userid'])
        print(user.first_name)
        message=Message.objects.get(id=request.POST['messageid'])
        print(message.content)
        Comment.objects.create(content=request.POST['comment'],poster=user,message=message)
    return redirect('./show_wall')

def delete_comment(request,id):
    this_comment=Comment.objects.get(id=id)
    this_comment_user=this_comment.poster.id
    current_user=request.session['userid']
    utc=pytz.UTC 
    created_at=this_comment.created_at
    now=utc.localize(datetime.now())
    # if the created_at + 30 minutes exceeds current time,
    if created_at + relativedelta(minutes=30) > now and this_comment_user == current_user:
        this_comment.delete()
        print("deleted a comment")
    else:
        #debug
        print("wrong user id to delete this comment or been more than 30 min")
    return redirect('../show_wall') 

def logout(request):
    request.session.clear()
    return redirect('/')