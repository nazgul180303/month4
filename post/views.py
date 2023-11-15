from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.


def hello_view(request):
    return HttpResponse('hello its my project')


def current_date(request):
    return HttpResponse(datetime.date.today())

def goodby(request):
    return HttpResponse('good bye')