from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    price= models.FloatField()
    stock=models.IntegerField()
    image_URL=models.CharField(max_length=2083)
    discount = models.FloatField(default=5)

class Offer(models.Model):
    code=models.CharField(max_length=30)
    description= models.CharField(max_length=50)
    discount=models.FloatField()
