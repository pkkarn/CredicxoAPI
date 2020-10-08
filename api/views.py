from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from api.serializers import *
from rest_framework.permissions import IsAuthenticated
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

# Admin View Setup


@api_view(['GET', 'POST'],)
def admin_view(request):
    users = User.objects.all()
    user = request.user
    permission_classes = (IsAuthenticated)
    # Checking user is super-admin or not
    if request.method == 'GET':
        if user.groups.filter(name='super-admin').exists():
            serializer = AdminSerializer(users, many=True)
            return Response(serializer.data)
        else:
            return Response({'response': 'You don\'t have access to see this'})
    else:
        serializer = RegisterationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Admin View Function For Update and Delete


@api_view(['GET', 'PUT', 'DELETE'])
def admin_update_view(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'GET':
        if request.user.groups.filter(name='super-admin').exists():
            serializer = AdminSerializer(user)
            return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AdminSerializer(user, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Student View


@api_view(['GET', ])
def student_view(request):
    user = User.objects.get(username=request.user)

    if request.method == 'GET':
        serializer = StudentSerializer(user)
        return Response(serializer.data)

# Teacher View


@api_view(['GET', 'POST'],)
def teacher_view(request):
    users = User.objects.filter(groups__name='student')
    user = request.user
    permission_classes = (IsAuthenticated)
    if request.method == 'GET':
        # Checking user is teacher or not
        if user.groups.filter(name='teacher').exists():
            serializer = TeacherSerializer(users, many=True)
            return Response(serializer.data)
        else:
            return Response({'respone': 'You\'re not  a teacher'})

    else:  # Post Request
        serializer = TeacherAddSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
