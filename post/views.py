from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.

from post.models import Product, Category


def products_view(request):
    if request.method == 'GET':
        post = Product.objects.all()
        return render(request, 'products/products.html', {'posts': post})


def product_detail(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        return render(request, 'products/detail.html', {'product': product})


def main_view(request):
    return render(request, 'layouts/main.html')


def category_view(request):
    categories = Category.objects.all()
    return render(request, 'products/category.html', {'category': categories})
