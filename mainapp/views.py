from django.shortcuts import render

from mainapp.models import ProductCategory


# Create your views here.

def products(request):
    title = 'каталог'
    links_menu = ProductCategory.objects.all()
    links_main_menu = [
        {'href': '/', 'name': 'домой', 'route': ''},
        {'href': '/products/', 'name': 'продукты', 'route': 'products/'},
        {'href': '/contact/', 'name': 'контакты', 'route': 'contact/'},
    ]

    context = {
        'title': title,
        'links_menu': links_menu,
        'links_main_menu': links_main_menu,
    }
    return render(request, 'mainapp/products.html', context=context)