from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accountapp.models import User
from accountapp.serializers import UserSerializer


class UserListView(APIView):
    def get(self,request):
        model = User.objects.all()
        serializer = UserSerializer(model, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    def get(self, request, user_id):
        model = User.objects.get(id = user_id)
        serializer = UserSerializer(model)
        return Response(serializer.data)

    def put(self, request, user_id):
        model = User.objects.get(id=request.data)

        serializer = UserSerializer(model, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)