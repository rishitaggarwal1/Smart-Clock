from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('/register', views.register, name="register"),
    path('/login', views.login, name="login"),
    path('/dashboard', views.dashboard, name="dashboard"),
    path('/set_Alarm', views.set_Alarm, name="set_Alarm"),
    path('/add_Event', views.add_Event, name="add_Event"),
    path('/reminder', views.reminder, name="reminder")
]
