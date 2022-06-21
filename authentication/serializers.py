from rest_framework import serializers
from authentication.models import CustomUser, MyUserManager


class CreateUser(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'nom', 'prenom')