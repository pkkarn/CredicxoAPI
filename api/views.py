from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from api.serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth.models import User

# Registeration API View


@api_view(['POST', ])
def resgisteration_view(request):
    if request.method == 'POST':
        serializer = RegisterationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Successfully Registered a new user"
            data['email'] = user.email
            data['username'] = user.username

        else:
            data = serializer.errors
        return Response(data)


# Admin View
class AdminView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        student = User.objects.filter()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
