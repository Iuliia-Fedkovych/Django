import json
from django.shortcuts import render


def main(request):
    context = {
        'title': 'home'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    related_products = [
        {'name': 'lamp',
         'short_desc': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
         'img': 'product-11.jpg'},
        {'name': 'chair',
         'short_desc': 'Steel frame, available in matt powder-coated black or highly polished chrome.',
         'img': 'product-21.jpg'},
        {'name': 'chair',
         'short_desc': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur',
         'img': 'product-31.jpg'}
    ]
    submenu = [
        {'href': 'products_all', 'name': 'all'},
        {'href': 'products_home', 'name': 'home'},
        {'href': 'products_office', 'name': 'office'},
        {'href': 'products_furniture', 'name': 'furniture'},
        {'href': 'products_modern', 'name': 'modern'},
        {'href': 'products_classic', 'name': 'classic'},

    ]
    context = {
        'title': 'products',
        'related_products': related_products,
        'submenu': submenu
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