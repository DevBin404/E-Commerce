from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product

class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = b