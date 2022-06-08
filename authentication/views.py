from django.shortcuts import render
from rest_framework import viewsets
from authentication.models import CustomUser, MyUserManager
from authentication.serializers import CreateUser


class UserViewSet(viewsets.ModelViewSet):

    queryset = CustomUser.objects.all()
    serializer_class = CreateUser