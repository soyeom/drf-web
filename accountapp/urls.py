from django.contrib import admin
from django.urls import path, include

from accountapp.api import UserList

urlpatterns = [
    path('api/',UserList.as_view()),
]