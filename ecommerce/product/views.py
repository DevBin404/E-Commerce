from itertools import product
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Category, Product, Image

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = "index.html"

    def get_queryset(self):
        products = Product.objects.all()
        for product in products:
            product.main_image = Image.objects.filter(product=product).first()

        return products

class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    queryset = Category.objects.all()
    template_name = 'pages/collection.html'

class SelectedCategoryListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = "index.html"

    def get_queryset(self):
        products = Product.objects.all()
        if self.kwargs['slug']:
            products = products.filter(category__slug=self.kwargs['slug'])
        for product in products:
            product.main_image = Image.objects.filter(product=product).first()
        return products