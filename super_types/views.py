from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import super_typesSerializer
from .models import super_types
from super_types import serializers


@api_view(['GET', 'POST'])
def super_types_list(request):
    
    if request.method == 'GET':
        super_types = super_types.objects.all()
        serializer = super_typesSerializer(super_types, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = super_typesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # if serializer.is_valid() == True:
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # else:
        #       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def super_types_detail(request, pk):
    super_types = get_object_or_404(super_types, pk=pk)
    if request.method == 'GET':
        serializer = super_typesSerializer(super_types);
        return Response(serializer.data)
    elif request.method == 'PUT': 
        serializer = super_typesSerializer(super_types, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super_types.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)