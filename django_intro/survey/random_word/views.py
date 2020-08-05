from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.

# initial starting state


def random_word(request):
    request.session['count'] = 0
    print("request.session[count]:", request.session['count'])
    return render(request, 'index2.html')


def current_status(request):
    # print("reached current_status()")
    # return HttpResponse("current status page")
    return render(request, 'index2.html')


def generate(request):
    # return HttpResponse("this is the generate() page")
    request.session['count'] += 1
    word = get_random_string(14)
    # print("word=", word)
    request.session['word'] = word
    return redirect('./current_status')


def reset(request):
    request.session.flush()
    return redirect('/random_word')
