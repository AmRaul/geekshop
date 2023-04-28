from django.shortcuts import render

from mainapp.models import Product

links_main_menu = [
        {'href': '/', 'name': 'домой', 'route': ''},
        {'href': '/products/', 'name': 'продукты','route': 'products/'},
        {'href': '/contact/', 'name': 'контакты', 'route': 'contact/'},
    ]
def index(request):
    title = 'GeekShop'
    products = Product.objects.all()[:4]

    context = {
        'title': title,
        'links_main_menu': links_main_menu,
        'products': products
    }
    return render(request, 'geekshop/index.html', context)

def contacts(request):
    title = 'контакты'
    context = {
        'title': title,
        'links_main_menu': links_main_menu,
    }
    return render(request, 'geekshop/contact.html', context)