from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This response is brought to you courtesy of index/views.py")