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
        if request.POST['set_alarm']:
            return render(request, 'set_Alarm.html', {})
        elif request.POST['add_event']:
            return render(request, 'add_Event', {})
    return render(request, 'dashboard.html', {})


def set_Alarm(request):
    return render(request, 'set_Alarm.html', {})


def add_Event(request):
    return render(request, 'add_Event', {})
