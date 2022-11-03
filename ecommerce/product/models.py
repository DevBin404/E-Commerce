from pyexpat import model
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(null=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    image = models.ImageField()
    count = models.IntegerField()
    is_guarantee = models.BooleanField()
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name




