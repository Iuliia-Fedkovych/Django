from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product

@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'admin/users'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': title,
        'objects': users_list,
    }

    return render(request, 'adminapp/users.html', context)

@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def user_update(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = 'admin/categories'

    categories_list = ProductCategory.objects.all()

    context = {
        'title': title,
        'objects': categories_list,
    }

    return render(request, 'adminapp/categories.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def category_update(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = 'admin/product'

    category = get_object_or_404(ProductCategory, pk=pk)

    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    context = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_read(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_update(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request):
    pass

