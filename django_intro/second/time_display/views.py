from django.shortcuts import render, redirect
from time import gmtime, strftime, localtime

# Create your views here.
def time_display(request):
    context={
        "current_time":strftime("%Y-%m-%d %H:%M ",localtime()),
        "gmtime":strftime("%Y-%m-%d %H:%M ",gmtime()),
        "name":"brian",
        "hobbies":["guitar","kickboxing","hiking","foreign languages"]
    }
    return render(request, 'index.html',context)