from django.shortcuts import render

from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from django.utils import timezone
from django.contrib.auth import authenticate
from datetime import date

# Create your views here.


class LoginApiView(APIView):

    def post(self, request, format=None):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            token = Token.objects.get_or_create(user=User.objects.get(username=username))
            print(token[0].key)
            return Response({
                "token": token[0].key
            }, status=status.HTTP_200_OK)

        return Response({
            "Error": "Invalid User"
        }, status=status.HTTP_400_BAD_REQUEST)