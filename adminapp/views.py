from authapp.models import ShopUser
from django.shortcuts import get_object_or_404, render
from mainapp.models import Product, ProductCategory
# Create your views here.

def users(request):
    title = 'админка/пользователи'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': title,
        'objects': users_list,
    }

    return render(request, 'adminapp/users.html', context)

def user_create(request):
    pass

def user_update(request):
    pass

def user_dalete(request):
    pass

def categories(request):
    title = 'админка/категории'

    categories_list = ProductCategory.objects.all()

    context = {
        'title': title,
        'objects': categories_list,
    }

    return render(request, 'adminapp/categories.html', context)

def category_create(request):
    pass

def category_update(request, pk):
    pass

def category_dalete(request, pk):
    pass

def products(request, pk):
    title = 'админка/продукты'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    context = {
        'title':title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html',context)


def product_read(request):
    pass

def product_create(request):
    pass

def product_update(request):
    pass

def product_dalete(request):
    pass

