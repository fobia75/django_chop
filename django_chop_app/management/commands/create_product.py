from django.core.management.base import BaseCommand
from ...models import Client, Product



class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        product = Product(name='Windshield', description='windshield for car', price= '25000', quantity_of_goods= '13')
        product.save()
        self.stdout.write(f'{product}')