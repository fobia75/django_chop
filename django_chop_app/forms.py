from django import forms
from .models import Product, Image


class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity_of_goods','product_added_date']


class ImageForm(forms.Form):
    image = forms.ImageField()



