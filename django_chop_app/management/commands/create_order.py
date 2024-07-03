from django.core.management.base import BaseCommand
from ...models import Order, Client, Product


class Command(BaseCommand):
    help = "Create order."

    def handle(self, *args, **kwargs):
        artur = Client.objects.create(name="artur")
        artur..create(connection_client="iPhone 8", price=67890)