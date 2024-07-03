from random import choices
from django.core.management.base import BaseCommand
from ...models import Client, Product, Order


class Command(BaseCommand):
    help = "Generate fake authors and posts."


    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='client ID')
    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'name_1{i}', email = f'email{i}@mail.ru', number_tel = f'898{i}{i}{i}{i}{i}{i}{i}{i}', client_address= f'rasha. ircutskaia obl g rirensk sovetskaya {i}', data_reg= '2000-11-1')
            client.save()
        for g in range(1, count + 1):
            product = Product(name=f'name_2{g}', description= f'description{g}', price = 1200, quantity_of_goods= 120, product_added_date= '2000-11-1')
            product.save()
        for j in range(1, count + 1):
            order = Order(connection_client = client, connection_product= product, date_ordered = '2000-11-12')
            order.save()