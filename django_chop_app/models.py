from django.utils import timezone
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length= 20)
    email = models.EmailField()
    number_tel = models.CharField(max_length=12, unique=True)
    client_address =  models.CharField(max_length= 100)
    data_reg = models.DateTimeField(auto_now_add = True)
    

    
class Product(models.Model):
    name = models.CharField(max_length= 20)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_of_goods = models.DecimalField(max_digits=10, decimal_places=2)
    product_added_date = models.DateTimeField(auto_now_add = True)


class Order(models.Model):
    connection_client = models.ForeignKey(Client, on_delete=models.CASCADE, null = True) 
    connection_product = models.ForeignKey(Product, on_delete=models.CASCADE, null = True) 
    date_ordered = models.DateTimeField(auto_now_add=True)



