from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, allow_unicode=True, auto_created=slugify(name))
    image = models.ImageField(upload_to='Categories', default='default/default.png')

    def get_absolute_url(self):
        return reverse("selected-category", args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(null=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    remaining_count = models.IntegerField()
    is_guarantee = models.BooleanField()
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='Products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='image')
    
