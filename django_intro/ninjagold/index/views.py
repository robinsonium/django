from django.shortcuts import render, redirect, HttpResponse
import random
from datetime import datetime

# When you start the game, your ninja should have 0 gold. The ninja can go to different places (farm, cave, house, casino) and earn different amounts of gold. In the case of a casino, your ninja can earn or lose up to 50 gold. Your job is to create a web app that allows this ninja to earn gold and to display past activities of this ninja.

# Guidelines
# Refer to the wireframe below.
# Have the four forms appear when the user goes to http://localhost:8000
# Use a hidden input tag in each form to pass the relevant location to the server
# Have /process_money determine how much gold the user should have

# Create your views here.


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, 'index.html')


def process_money(request):
    now = datetime.now().strftime("%m/%d/%Y %H:%M")
    multiplier = {
        'farm': (10, 20),
        'cave': (5, 10),
        'house': (2, 5),
        'casino': (0, 50),
    }
    location = request.POST['location']
    current_gold = random.randint(
        multiplier[location][0], multiplier[location][1])
    request.session['gold'] += current_gold
    
    request.session['activities'].append({"earned":current_gold,"time":now})
    print(request.session['activities'])
    return redirect('/')
    # return HttpResponse("placeholder for process_money()")


def reset(request):
    request.session.flush()
    return redirect('/')
