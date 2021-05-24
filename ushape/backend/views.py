from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.models import Calorielist
from backend.serializers import CalorielistSerializer

#auth tokens
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics

@api_view(['GET', 'POST'])
def calorielist_list(request, format=None):
    """
    List all code products, or create a new product.
    """
    if request.method == 'GET':
        product = Calorielist.objects.all()
        serializer = CalorielistSerializer(product, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CalorielistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def calorielist_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code product.
    """
    try:
        product = Calorielist.objects.get(pk=pk)
    except Calorielist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CalorielistSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CalorielistSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer