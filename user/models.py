from django.db import models

# Create your models here.
class Data_Users(models.Model):
     id = models.AutoField(primary_key=True)
     name=models.CharField(max_length=100)
     email=models.EmailField(max_length=200)
     roll=models.CharField(max_length=200)
     
