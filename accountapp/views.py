from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.views import APIView


# Create your views here.
class Login(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if email is None or password is None:
            return Response({'error' : 'Please both username and password'}, status=HTTP_400_BAD_REQUEST)

        user = authenticate(email=email, password=password)

        if not user:
            return Response({'error' : 'Invalid credentials'}, status=HTTP_404_NOT_FOUND)

        token = Token.objects.create(user=user)

        return Response({'message':"hello_world_drf!"})