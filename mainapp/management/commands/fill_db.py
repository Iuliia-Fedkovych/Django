import os
import json

from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from django.contrib.auth.models import User
from authapp.models import ShopUser


JSON_PATH = 'mainapp/json'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'),
              'r',
              encoding='utf-8') as file:
        return json.load(file)


class Command(BaseCommand):
    help = 'Fill DB new Data'

    def handle(self, *args, **kwargs):
        categories = load_from_json('categories')
        ProductCategory.objects.all().delete()

        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = load_from_json('products')

        Product.objects.all().delete()

        for product in products:
            category_name = product['category']
            product['category'] = ProductCategory.objects.get(name=category_name)
            new_product = Product(**product)
            new_product.save()

        # Создаем суперпользователя при помощи менеджера модели
        super_user = ShopUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains', age=30)