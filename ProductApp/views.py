from django.shortcuts import render
from django.views.generic import DetailView
from ProductApp.models import Product


class ProductView(DetailView):
    template_name = 'ProductApp/product-detail.html'
    model = Product
