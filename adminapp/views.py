from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory
from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm, ProductEditForm


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
    title = 'users/create'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = ShopUserRegisterForm()
    context = {
        'title': title,
        'update_form': user_form,
        }
    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'users/edit'

    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:user_update', args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)
    context = {
        'title': title,
        'update_form': edit_form,
        }
    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'user/delete'

    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin:users'))

    context = {
        'title': title,
        'user_to_delete': user,
    }
    return render(request, 'adminapp/user_delete.html', context)


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
    title = 'categories/create'

    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        category_form = ProductCategoryEditForm()
    context = {
        'title': title,
        'update_form': category_form,
        }
    return render(request, 'adminapp/category_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    title = 'categories/edit'

    edit_category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:category_update', args=[edit_category.pk]))
    else:
        edit_form = ProductCategoryEditForm(instance=edit_category)
    context = {
        'title': title,
        'update_form': edit_form,
        }
    return render(request, 'adminapp/category_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    title = 'category/delete'

    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse('admin:categories'))

    context = {
        'title': title,
        'category_to_delete': category,
    }
    return render(request, 'adminapp/category_delete.html', context)



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
def product_create(request, pk):
    title = 'product/create'
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin:products',
                                                args=[pk]))
    else:
        product_form = ProductEditForm(initial={'category': category})
    context = {
        'title': title,
        'update_form': product_form,
        'category': category,
    }
    return render(request, 'adminapp/product_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_read(request, pk):
    title = 'product/details'

    product = get_object_or_404(Product, pk=pk)

    context = {
        'title': title,
        'object': product,
    }
    return render(request, 'adminapp/product_read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    title = 'product/edit'

    edit_product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES,
                                    instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:product_update',
                                                args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)
    context = {
        'title': title,
        'update_form': edit_form,
        'category': edit_product.category
    }
    return render(request, 'adminapp/product_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    title = 'product/delete'

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.is_active = False
        product.save()
        return HttpResponseRedirect(reverse('admin:products',
                                            args=[product.category.pk]))
    context = {
        'title': title,
        'product_to_delete': product,
    }
    return render(request, 'adminapp/product_delete.html', context)

