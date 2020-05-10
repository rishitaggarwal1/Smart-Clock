from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def register(request):
    return render(request, 'register.html', {})


def login(request):
    return render(request, 'login.html', {})


def dashboard(request):
    if request.method == "POST":
        if 'set_alarm' in request.POST:
            return render(request, 'set_Alarm.html', {})
        elif 'add_event' in request.POST:
            return render(request, 'add_Event.html', {})
    return render(request, 'dashboard.html', {})


def set_Alarm(request):
    return render(request, 'set_Alarm.html', {})


def add_Event(request):
    return render(request, 'add_Event.html', {})
