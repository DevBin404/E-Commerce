
from django.contrib import admin
from .models import Product, Image, Category


class ImageAdmin(admin.TabularInline):
    model = Image

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]

admin.site.register(Product, ProductAdmin)
admin.site.register(Image)
admin.site.register(Category)