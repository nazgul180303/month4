from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.

from post.models import Product

def products_view(request):
    if request.method == 'GET':
      post = Product.objects.all()
      return render(request, 'products/products.html', {'posts': post})


def main_view(request):
    return render(request, 'layouts/main.html')
#def current_date(request):
   # return HttpResponse(datetime.date.today())

#def goodby(request):
  #  return HttpResponse('good bye')

#def islam (request):
  #  if request.method == 'GET':

     #    return HttpResponse('islam')