import json
from django.shortcuts import render
from .models import ProductCategory, Product



def main(request):
    products = Product.objects.all()
    context = {
        'title': 'home',
        'products': products,
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    submenu = [
        {'href': 'products_all', 'name': 'all'},
        {'href': 'products_home', 'name': 'home'},
        {'href': 'products_office', 'name': 'office'},
        {'href': 'products_furniture', 'name': 'furniture'},
        {'href': 'products_modern', 'name': 'modern'},
        {'href': 'products_classic', 'name': 'classic'},

    ]

    products = Product.objects.all()[:3]
    categories = ProductCategory.objects.all()

    context = {
        'title': 'products',
        'products': products,
        'categories': categories
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    with open('geekshop/locations.json', 'r', encoding='utf-8') as f:
        locations = json.load(f)

    context = {
        'title': 'contacts',
        'locations': locations
    }
    return render(request, 'mainapp/contact.html', context)