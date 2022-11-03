from pyexpat import model
from django.db import models

class Category(models.Model):
    name = model.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(null=True)
    price = models.DecimalField(decimal_place=2, max_digit=6)
    image = models.ImageField()
    count = models.IntegerField()
    is_guarantee = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)




