from django.db import models
from catagory.models import *
# Create your models here.

class Task(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.TextField()
    #data type catagry  objects from catagory model
    catagoryid=models.ForeignKey('catagory.Catagory',on_delete=models.CASCADE)