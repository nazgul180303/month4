from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime

from post.forms import ProductCreateForms, CategoryCreateForm, ReviewCreateForm
# Create your views here.

from post.models import Product, Category, Review


def products_view(request):
    if request.method == 'GET':
        post = Product.objects.all()
        return render(request, 'products/products.html', {'posts': post})


def product_detail(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        reviews = Review.objects.all()
        context = {
            'product': product,
            'reviews': reviews,
        }
        return render(request, 'products/detail.html', context=context)
    elif request.method == 'POST':
        form = ReviewCreateForm(request.POST)
        if form.is_valid():
            Review.objects.create(**form.cleaned_data)
            return redirect(f'/product/{id}')
        context = {'form': form}

        return render(request, 'products/detail.html', context=context)

def main_view(request):
    return render(request, 'layouts/main.html')


def category_view(request):
    categories = Category.objects.all()
    return render(request, 'products/category.html', {'category': categories})


def product_create(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForms
        }
        return render(request, template_name='products/create.html', context=context)
    elif request.method == 'POST':
        form = ProductCreateForms(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return redirect('/product/')
        context = {
            'form': form
        }
        return render(request, template_name='products/create.html', context=context)


def category_create(request):
    if request.method == "GET":
        context = {
            'form': CategoryCreateForm
        }
        return render(request, template_name='category/create.html', context=context)
    elif request.method == 'POST':
        form = CategoryCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect('/category/')
        context = {
            'form': form
        }
        return render(request, template_name='category/create.html', context=context)
