import random

from django.core.management import BaseCommand
import argparse
from marketplace.models import Product


class Command(BaseCommand):
    help = 'Generate new product'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            product = Product(name=f'Name{i}',
                              price=random.randint(1, 100),
                              description=f'description{i}',
                              quantity=random.randint(1, 10),
                              date_added='2000-01-01')
            product.save()
            self.stdout.write(f'{product}')