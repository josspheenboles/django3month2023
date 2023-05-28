from django.db import models

# Create your models here.
class Catagory(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    def __str__(self):
        return str(self.id) +' '+self.name