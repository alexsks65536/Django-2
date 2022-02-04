import os
import random

from django.core.serializers import json
from django.shortcuts import render
from django.template.defaultfilters import title

from .management.commands.fill_db import JSON_PATH
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def main(request):
    title = "главная"
    products = Product.objects.filter(
        is_active=True, category__is_active=True
    ).select_related("category")[:3]

    content = {
        "title": title,
        "products": products,
    }

    return render(request, "mainapp/index.html", content)


menu_links = [
    {"href": "/", "name": "домой"},
    {"href": "/products", "name": "продукты"},
    {"href": "/contact", "name": "контакты"},
]


def contact(request):
    return render(
        request,
        "mainapp/contact.html",
        context={
            "menu_links": menu_links,
        },
    )


def basket(request, links_menu=None, pk=None):

    if pk:
        if pk == "0":
            products = Product.objects.all().order_by("price")
            category = {"name": "все"}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by("price")

        content = {
            "title": title,
            "links_menu": links_menu,
            "category": category,
            "products": products,
        }

    return render(request, "mainapp/products_list.html", content)


def get_hot_product():
    products = Product.objects.all()

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(
        pk=hot_product.pk
    )[:3]

    return same_products


def product(request, pk):
    title = "продукты"

    content = {
        "title": title,
        "links_menu": ProductCategory.objects.all(),
        "product": get_object_or_404(Product, pk=pk),
    }

    return render(request, "mainapp/product.html", content)


def products(request, pk=None, page=1):
    title = "продукты"
    links_menu = ProductCategory.objects.filter(is_active=True)

    if pk is not None:
        if pk == 0:
            category = {"pk": 0, "name": "все"}
            products = Product.objects.filter(
                is_active=True, category__is_active=True
            ).order_by("price")
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(
                category__pk=pk, is_active=True, category__is_active=True
            ).order_by("price")

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            "title": title,
            "links_menu": links_menu,
            "category": category,
            "products": products_paginator,
        }

        return render(request, "mainapp/products_list.html", content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        "title": title,
        "links_menu": links_menu,
        "hot_product": hot_product,
        "same_products": same_products,
    }

    return render(request, "mainapp/products.html", content)


def load_from_json(file_name):
    with open(
        os.path.join(JSON_PATH, file_name + ".json"), "r", errors="ignore"
    ) as infile:
        return json.load(infile)
