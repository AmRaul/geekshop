from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    product_name = models.CharField(
        verbose_name='Название продукта',
        max_length=64,
        unique=True,
    )
    description = models.TextField(
        verbose_name='Описание продукта',
        blank=True,
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.product_name


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='Название товара',
        max_length=128,
    )
    image = models.ImageField(
        upload_to='products_images',
        blank=True,
    )
    short_desc = models.CharField(
        verbose_name='Краткое описание',
        max_length=60,
        blank=True,
    )
    description = models.TextField(
        verbose_name='Описание товара',
        blank=True,
    )
    price = models.DecimalField(
        verbose_name='Цена товара',
        max_digits=8,
        decimal_places=2,
        default=0,
    )
    quentity = models.PositiveIntegerField(
        verbose_name='количество на складе',
        default=0,
    )

    def __str__(self):
        return f'{self.name} ({self.category.product_name})'
