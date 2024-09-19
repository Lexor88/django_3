from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Load data from fixtures into the database'

    def handle(self, *args, **kwargs):
        # Удаляем все данные из моделей перед загрузкой
        call_command('flush', interactive=False)

        # Загрузка данных из фикстуры
        call_command('loaddata', 'catalog/fixtures/catalog_data.json')

        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))
