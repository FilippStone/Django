from django.core.management.base import BaseCommand
from marketplace.models import Order, Client, Product
import random


class Command(BaseCommand):
    help = 'Create orders'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        clients = Client.objects.all()
        for c in Product.objects.all():
            for i in range(1, count + 1):
                client = clients[random.randint(0, len(clients) - 1)]
                order = Order(total_amount=random.randint(1, 10),
                              order_date='2000-01-01',
                              client=client)
                order.save()
                order.product.set([c])
                self.stdout.write(f'{order}')