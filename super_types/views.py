from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperTypeSerializer
from .models import SuperType
from super_types import serializers


@api_view(['GET', 'POST'])
def super_types_list(request):
    
    if request.method == 'GET':
        
        # type_name = request.query_params.get('super_type')
        # print(type_name)
        
        super_types = SuperType.objects.all()

        # if type_name:
        #     super_types = super_types.filter(type__name=type_name)
        # if type_name:
        #     super_types = super_types.filter(type__name=type_name)
        
        serializer = SuperTypeSerializer(super_types, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuperTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # if serializer.is_valid() == True:
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # else:
        #       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def super_types_detail(request, pk):
    super_type = get_object_or_404(SuperType, pk=pk)
    if request.method == 'GET':
        serializer = SuperTypeSerializer(super_type);
        return Response(serializer.data)
    elif request.method == 'PUT': 
        serializer = SuperTypeSerializer(super_type, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)