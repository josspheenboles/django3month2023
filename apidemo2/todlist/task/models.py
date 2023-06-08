from django.db import models

# Create your models here.
class Catagory(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)

class Task(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    catgoryid=models.ForeignKey(Catagory,on_delete=models.CASCADE)
