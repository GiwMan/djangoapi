from queue import PriorityQueue
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from products.models import Product
from products.serialize import ProductSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def api_home(request, *args, **kwargs):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        