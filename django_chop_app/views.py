from datetime import date, datetime, timedelta
from random import choice
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from .models import Order, Client, Product
from django.shortcuts import render, get_object_or_404


def index(request):
    clientes = Client.objects.all()
    
    return render(request, "index.html", {"clientes": clientes})


def create(request):
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        client = Client()
        client.name = request.POST.get("name")
        client.email= request.POST.get("email")
        client.number_tel = request.POST.get("number_tel")
        client.client_address = request.POST.get("client_address")
        client.data_reg = request.POST.get("data_reg")
        client.save()
        return HttpResponseRedirect("/")
    # передаем данные в шаблон
    clientes = Client.objects.all()
    print(clientes)
    return render(request, "create.html", {"clientes": clientes})


def create_product(request):
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        product = Product()
        product.name = request.POST.get("name")
        product.description= request.POST.get("description")
        product.price = request.POST.get("price")
        product.quantity_of_goods = request.POST.get("quantity_of_goods")
        product.product_added_date = request.POST.get("product_added_date")
        product.save()
        return HttpResponseRedirect("/")
    # передаем данные в шаблон
    productes = Product.objects.all()
    
    return render(request, "create_productes.html", {"productes": productes})


def create_order(request):
    if request.method == "POST":
        client = Client.objects.create(name='Cic', email='cic@example.com', number_tel= '19261230912', client_address= 'rasha. ircutskaia obl g rirensk sovetskaya 920')
        product_1 = Product.objects.create(name="samsung galacsi", description='windshield for car', price= '25000', quantity_of_goods= '13')
        product_2 = Product.objects.create(name="samsung galacsi11", description='windshield for car', price= '22000', quantity_of_goods= '11')
        client_product_1 = Order(connection_client= client, connection_product= product_1, total_price= 1000)
        client_product_2 = Order(connection_client= client, connection_product= product_2, total_price= 2000)
        client_product_1.save()
        client_product_2.save()
        return HttpResponseRedirect("/")
    orders = Order.objects.get(connection_client= client).name.all()
    return render(request, "create_order.html", {"orders": orders})


def create_list_7(request):
    date = datetime.now()
    new_date = date - timedelta(days = 7)
    # orders = Order.objects.filter(date_ordered__month__gt = 5)
    orders = Order.objects.filter(date_ordered__date__gt = new_date)
    return render(request, "create_list_7.html", {"orders": orders})


def create_list_30(request):
    date = datetime.now()
    new_date = date - timedelta(days = 30)
    # orders = Order.objects.filter(date_ordered__month__gt = 5)
    orders = Order.objects.filter(date_ordered__date__gt = new_date)
    return render(request, "create_list_30.html", {"orders": orders})


def create_list_365(request):
    date = datetime.now()
    new_date = date - timedelta(days = 364)
    orders = Order.objects.filter(date_ordered__date__gt = new_date)
    return render(request, "create_list_365.html", {"orders": orders})





