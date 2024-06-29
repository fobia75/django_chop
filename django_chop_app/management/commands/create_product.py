from django.core.management.base import BaseCommand
from ...models import Client, Product



class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        product = Product(name='compressor', description='compressor for air system operation', price= '25000', quantity_of_goods= '130')
        product.save()
        self.stdout.write(f'{product}')