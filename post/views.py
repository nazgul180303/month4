from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime
from django.db.models import Q

from djangoProject.settings import PAGE_SIZE
from post.forms import ProductCreateForms, CategoryCreateForm, ReviewCreateForm
# Create your views here.

from post.models import Product, Category, Review

PAGINATION_LIMIT = 3
def products_view(request):
    if request.method == 'GET':
        posts = Product.objects.all().order_by('-name', 'created_ad')
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        ''' start_with, ends_with, icontains '''

        '''and | or'''

        if search:
            posts = posts.filter(name__icontains=search) | posts.filter(description__icontains=search)

        max_page = posts.__len__() / PAGINATION_LIMIT
        max_page = round(max_page) + 1 if round(max_page) < max_page else round(max_page)

        ''' posts splice'''
        posts = posts[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        context = {
            'posts': posts,
            'pages': range(1, max_page + 1)
        }

        return render(request, 'products/products.html', context=context)

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


