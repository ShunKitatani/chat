
from django.contrib import admin
from django.urls import path, include
from .views import index, room, signupfunc, loginfunc, logoutfunc

urlpatterns = [
    path('signup/', signupfunc, name='signup' ),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
    path('index/', index, name='index'),
    path('room/<int:pk>', room, name='room'),
]
