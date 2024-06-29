from django.shortcuts import render
from random import choice
from django.http import HttpResponse
from .models import Order, Client, Product


def index(request):
    return HttpResponse('hello world')