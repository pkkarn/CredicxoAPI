from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from api.serializers import RegisterationSerializer

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
