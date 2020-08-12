import json
import random
from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .models import ProductCategory, Product

def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []

def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]

    return same_products


def main(request):
    products = Product.objects.all()
    basket = get_basket(request.user)

    context = {
        'title': 'home',
        'products': products,
        'basket':basket,
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    print(pk)
    title = 'products'
    categories = ProductCategory.objects.all()

    basket = get_basket(request.user)


    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'all'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')
        context = {
            'title': title,
            'products': products,
            'categories': categories,
            'category': category,
            'basket':basket
        }
        return render(request, 'mainapp/products_list.html', context)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    context = {
        'title': title,
        'hot_product': hot_product,
        'same_products': same_products,
        'categories': categories,
        'basket': basket
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    with open('mainapp/json/locations.json', 'r', encoding='utf-8') as f:
        locations = json.load(f)

    basket = get_basket(request.user)

    context = {
        'title': 'contacts',
        'locations': locations,
        'basket': basket,
    }
    return render(request, 'mainapp/contact.html', context)


def product(request, pk):
    context = {
        'title': 'product',
        'categories': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/product.html', context)
