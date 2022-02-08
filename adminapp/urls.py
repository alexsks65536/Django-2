"""adminapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import adminapp.views as adminapp
from django.urls import path

app_name = "adminapp"

urlpatterns = [
    path("users/create/", adminapp.user_create, name="user_create"),
    path("users/read/", adminapp.UsersListView.as_view(), name="users"),
    path("users/update/<int:pk>/", adminapp.user_update, name="user_update"),
    path("users/delete/<int:pk>/", adminapp.user_delete, name="user_delete"),
    path(
        "categories/create/",
        adminapp.ProductCategoryCreateView.as_view(),
        name="category_create",
    ),
    path("categories/read/", adminapp.categories, name="categories"),
    path(
        "categories/update/<int:pk>/",
        adminapp.ProductCategoryUpdateView.as_view(),
        name="category_update",
    ),
    path(
        "categories/delete/<int:pk>/",
        adminapp.ProductCategoryDeleteView.as_view(),
        name="category_delete",
    ),
    path(
        "products/create/category/<int:pk>/",
        adminapp.product_create,
        name="product_create",
    ),
    path("products/read/category/<int:pk>/", adminapp.products, name="products"),
    path(
        "products/read/<int:pk>/",
        adminapp.ProductDetailView.as_view(),
        name="product_read",
    ),
    path("products/update/<int:pk>/", adminapp.product_update, name="product_update"),
    path("products/delete/<int:pk>/", adminapp.product_delete, name="product_delete"),
]
