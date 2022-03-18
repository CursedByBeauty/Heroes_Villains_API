from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import supersSerializer
from .models import supers
from supers import serializers


@api_view(['GET', 'POST'])
def supers_list(request):
    
    if request.method == 'GET':
        supers = supers.objects.all()
        serializer = supersSerializer(supers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = supersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # if serializer.is_valid() == True:
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # else:
        #       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    supers = get_object_or_404(supers, pk=pk)
    if request.method == 'GET':
        serializer = supersSerializer(supers);
        return Response(serializer.data)
    elif request.method == 'PUT': 
        serializer = supersSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)