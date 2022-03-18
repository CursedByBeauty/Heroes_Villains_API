from dataclasses import fields
from rest_framework import serializers
from .models import supers

class supersSerializer(serializers.ModelsSerializer):
    class Meta:
        model = supers
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'seconday_ability', 'catchphrase', 'super_types']