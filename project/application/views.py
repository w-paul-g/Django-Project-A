from django.shortcuts import render
from application.models import Customer
from application.serializers import CustomerSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET', 'POST'])
def customer_list(request):
    if request.method == 'GET':
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return JsonResponse({'customer':  serializer.data}, safe=False)
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
