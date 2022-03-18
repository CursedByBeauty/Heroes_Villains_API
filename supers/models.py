from django.db import models
from super_types.models import super_types
# Create your models here.


class supers(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    seconday_ability = models.CharField(max_length=255)
    catchphrase = models.CharField(max_length=255)
    super_types = models.ForeignKey(super_types, on_delete=models.CASCADE)