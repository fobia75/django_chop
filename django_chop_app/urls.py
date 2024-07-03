
from django.contrib import admin
from django.urls import path, include
from .views import index, create, create_product, create_order, create_list_7, create_list_30

urlpatterns = [
    path('', index, name= 'index'),
    path('create/', create, name= 'create'),
    path('create_product/', create_product, name= 'create_product'),
    path('create_order/', create_order, name= 'create_order'),
    path('create_list_7/', create_list_7, name= 'create_list_7'),
    path('create_list_30/', create_list_30, name= 'create_list_30'),
    path('create_list_365/', create_list_30, name= 'create_list_30'),

]
