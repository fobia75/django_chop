from django.core.management.base import BaseCommand
from ...models import Client
from django.utils import timezone



class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(name='nic', email='nic@example.com', number_tel= '89261230912', client_address= 'rasha. ircutskaia obl g rirensk sovetskaya 20')
        client.save()
        self.stdout.write(f'{client}')
