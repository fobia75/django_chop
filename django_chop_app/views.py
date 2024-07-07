from datetime import date, datetime, timedelta
from random import choice
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from .models import Order, Client, Product
from django.shortcuts import render, get_object_or_404
from .forms import ImageForm, ProductForms
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render



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
    if request.method == 'POST':
        form = ProductForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity_of_goods = form.cleaned_data['quantity_of_goods']
            product_added_date  = form.cleaned_data['product_added_date']
            product = Product(name= name, description= description, price= price, quantity_of_goods= quantity_of_goods, product_added_date= product_added_date)
            product.save()
            return render(request, 'create_productes.html', {'answer': 'продукт добавлен'} )  
    else:
        form = ProductForms() 
    return render(request, 'create_productes.html', {'form': form} )


def create_order(request):
    if request.method == "POST":
        client = Client.objects.create(name='Cic', email='cic@example.com', number_tel= '19261230912', client_address= 'rasha. ircutskaia obl g rirensk sovetskaya 920')
        product_1 = Product.objects.create(name="samsung galacsi", description='windshield for car', price= '25000', quantity_of_goods= '13')
        product_2 = Product.objects.create(name="samsung galacsi11", description='windshield for car', price= '22000', quantity_of_goods= '11')
        client_product_1 = Order(connection_client= client, connection_product= product_1, total_price= Order.total_price())
        client_product_2 = Order(connection_client= client, connection_product= product_2, total_price= Order.total_price())
        client_product_1.save()
        client_product_2.save()
        print(*client_product_1)
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


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form':form})






