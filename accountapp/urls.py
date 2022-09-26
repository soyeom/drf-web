from django.contrib import admin
from django.urls import path, include

from accountapp.api import UserListView, UserDetailView

urlpatterns = [
    path('user_list',UserListView.as_view()),
    path('user_list/<int:user_id>',UserDetailView.as_view()),
    path('rest_auth/register',include('dj_rest_auth.registration.urls')),
    path('rest_auth', include('dj_rest_auth.urls')),
]