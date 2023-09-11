from django.core.management import BaseCommand
from random import randint
from myapp2.models import GameModel


class Command(BaseCommand):
    help = 'Play game Head and Tails'

    def handle(self, *args, **kwargs):
        result = ('Tails', 'Head')[randint(0, 1)]

        game = GameModel(result=result)
        game.save()

        self.stdout.write(f'{game}')
