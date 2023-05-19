from django.shortcuts import render, get_object_or_404

from mainapp.models import ProductCategory, Product


# Create your views here.

def products(request, pk=None):
    title = 'каталог'
    links_menu = ProductCategory.objects.all()
    links_main_menu = [
        {'href': '/', 'name': 'домой', 'route': ''},
        {'href': '/products/', 'name': 'продукты', 'route': 'products/'},
        {'href': '/contact/', 'name': 'контакты', 'route': 'contact/'},
    ]

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'links_menu': links_menu,
            'links_main_menu': links_main_menu,
            'products': products,
            'category': category,
        }
        return render(request, 'mainapp/products.html', context=context)

    same_products = Product.objects.all()

    context = {
        'title': title,
        'links_menu': links_menu,
        'links_main_menu': links_main_menu,
        'products': same_products,
    }
    return render(request, 'mainapp/products.html', context=context)