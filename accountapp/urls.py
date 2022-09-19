from django.urls import path, include
from rest_framework.authtoken import views

from accountapp.views import Login

urlpatterns = [
    path('login/', Login.as_view()),
    path('auth/', views.obtain_auth_token, name='user_auth-create'),
]