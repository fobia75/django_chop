from django.contrib import admin
from .models import Product, Client, Order


def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity_of_goods = 0)


class AdminClient(admin.ModelAdmin):
    list_display = ('name','email', 'number_tel', 'client_address', 'data_reg',)
    list_filter = ('name',)
    search_fields = ('name','data_reg',)


class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity_of_goods', 'product_added_date',)
    """Отдельный продукт."""
    # fields = ('name', 'description', )
    # readonly_fields = ['product_added_date', 'quantity_of_goods',]
    fieldsets = [['test', {'fields': ['name', 'description']}],]
    actions = [reset_quantity]
    


admin.site.register(Client, AdminClient)
admin.site.register(Product, AdminProduct)
admin.site.register(Order)
