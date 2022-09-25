from django.contrib import admin
from django.urls import path, include

from accountapp.api import UserListView, UserDetailView

urlpatterns = [
    path('api/user_list',UserListView.as_view()),
    path('api/user_list/<int:user_id>',UserDetailView.as_view()),
]