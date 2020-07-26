from django.shortcuts import render


def main(request):
    context = {
        'title': 'home'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    same_products = []
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
        'same-products': same_products,
        'submenu': submenu
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    context = {
        'title': 'contacts'
    }
    return render(request, 'mainapp/contact.html', context)