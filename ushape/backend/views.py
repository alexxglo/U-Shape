from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.models import Calorielist
from backend.serializers import CalorielistSerializer

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