from time import sleep
from django.core.management import BaseCommand
from power.addGeneratorData import add_generator_data


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = add_generator_data()
        print(data)