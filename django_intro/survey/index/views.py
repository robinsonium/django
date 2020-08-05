from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, 'index.html')


def result(request):
    if request.method == "POST":
        print("keys",request.POST.keys())
        print("values",request.POST.values())
        for key in request.POST.keys():
            if key:
                request.session[key] = request.POST[key]
    return redirect('/render_result')


def render_result(request):
    return render(request, 'result.html')


def start_over(request):
    request.session.flush()
    return redirect('/')