from rest_framework import serializers
from .models import *
from django.db.models import fields

class Catagoryselizer(serializers.ModelSerializer):
    class Meta:
        model=Catagory
        fields ='__all__'
