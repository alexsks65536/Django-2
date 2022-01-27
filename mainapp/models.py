from decimal import Decimal
from django.db import models
from django.db.models.fields import DecimalField, FloatField, IntegerField
from django.db.models.fields.related import ForeignKey


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="имя", max_length=64, unique=True)
    description = models.TextField(verbose_name="описание", blank=True)
    is_active = models.BooleanField(verbose_name="активна", default=True)


def __str__(self):
    return self.name


class Product(models.Model):
    objects = None
    name = models.CharField(verbose_name="имя", max_length=128, unique=True)
    description = models.TextField(verbose_name="описание", blank=True, null=True)
    category = ForeignKey(
        ProductCategory, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )
    short_description = models.CharField(
        verbose_name="короткое описание", max_length=64, blank=True
    )
    price = models.DecimalField(
        verbose_name="цена продукта", max_digits=8, decimal_places=2, default=0
    )
    price_with_discount = models.DecimalField(
        verbose_name="цена со скидкой", max_digits=8, decimal_places=2, default=0
    )
    quantity = models.PositiveIntegerField(
        verbose_name="Количество на складе", default=0
    )
    image = models.ImageField(upload_to="products_images", blank=True)
    is_active = models.BooleanField(verbose_name="В каталоге", default=True)
