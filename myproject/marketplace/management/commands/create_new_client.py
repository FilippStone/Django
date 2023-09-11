from django.core.management import BaseCommand
import argparse
from marketplace.models import Client


class Command(BaseCommand):
    help = 'Generate new client'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'Name{i}',
                            email=f'Mail{i}@mail.ru',
                            phone_number=f'Phone{i}',
                            address=f'Addres{i}',
                            registration_date='2000-01-01')
            client.save()
            self.stdout.write(f'{client}')
