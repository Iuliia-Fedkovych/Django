import json
from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .models import ProductCategory, Product

def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []

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

    products = Product.objects.all()[:3]

    context = {
        'title': title,
        'products': products,
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
