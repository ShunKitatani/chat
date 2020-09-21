
from django.contrib import admin
from django.urls import path, include
from .views import index, room

urlpatterns = [
    path('index/', index, name='index'),
    path('room/<int:pk>', room, name='room'),
]
