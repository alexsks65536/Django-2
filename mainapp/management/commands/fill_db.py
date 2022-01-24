from django.core.management.base import BaseCommand
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


import json, os

JSON_PATH = "mainapp/json"


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + ".json"), "r") as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json("categories")

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = load_from_json("products")

        Product.objects.all().delete()
        for product in products:
            category_name = product["category"]
            # Получаем категорию по имени
            _category = ProductCategory.objects.get(name=category_name)
            # Заменяем название категории объектом
            product["category"] = _category
            new_product = Product(**product)
            new_product.save()

        # Создаем суперпользователя при помощи менеджера модели

        super_user = ShopUser.objects.create_superuser(
            "django",
            "django@geekshop.local",
            "geekbrains",
            age=33,
            avatar="users_avatars/superadmin.jpg",
        )
        user = ShopUser.objects.create_superuser(
            "user", "django@geekshop.local", "geekbrains", age=18
        )
        user = ShopUser.objects.create_superuser(
            "Schwarzenegger",
            "schwarz@hollywood.cinema",
            "geekbrains",
            age=74,
            avatar="users_avatars/schwarzenegger.jpg",
        )
        user = ShopUser.objects.create_superuser(
            "Tarantino",
            "tarantino@hollywood.cinema",
            "geekbrains",
            age=58,
            avatar="users_avatars/tarantino.jpg",
        )
        user = ShopUser.objects.create_superuser(
            "Sigourney Weaver",
            "Weaver@hollywood.cinema",
            "geekbrains",
            age=72,
            avatar="users_avatars/sigurni.jpg",
        )
