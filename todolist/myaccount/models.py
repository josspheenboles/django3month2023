from django.db import models

# Create your models here.
class MyUser(models.Model):
    #int auto pk
    id=models.AutoField(primary_key=True,db_column='ID')
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=12)
    email=models.EmailField(max_length=100)
    actiiv=models.BooleanField()
