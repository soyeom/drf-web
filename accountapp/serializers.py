from rest_framework import serializers

from accountapp.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)

    class Meta:
        model=User
        fields='__all__'