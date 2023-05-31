from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/read/', adminapp.users, name='users'),
    path('users/update/', adminapp.user_update, name='user_update'),
    path('users/delete/', adminapp.user_dalete, name='user_delete'),

    path('categories/create/', adminapp.category_create, name='category_create'),
    path('categories/read/', adminapp.categories, name='categories'),
    path('categories/update/<int:pk>/', adminapp.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', adminapp.category_dalete, name='category_dalete'),

    path('products/create/category/<int:pk>/', adminapp.product_create, name='product_create'),
    path('products/read/category/<int:pk>/', adminapp.products, name='products'),
    path('products/read/<int:pk>/', adminapp.product_read, name='product_read'),
    path('products/update/category/<int:pk>/', adminapp.product_update, name='product_update'),
    path('products/delete/category/<int:pk>/', adminapp.product_dalete, name='product_dalete'),
]
