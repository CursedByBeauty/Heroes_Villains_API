from dataclasses import field, fields
from rest_framework import serializers
from .models import super_types

class super_typesSerializer(serializers.ModelSerializer):
    class Meta:
        model = super_types
        fields = ['id', 'type']