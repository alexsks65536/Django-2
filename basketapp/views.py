from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_delete

from basketapp.models import Basket
from mainapp.models import Product
from ordersapp.models import OrderItem


@login_required
def basket(request):
    title = "корзина"
    basket_items = Basket.objects.filter(user=request.user).order_by(
        "product__category"
    )

    content = {
        "title": title,
        "basket_items": basket_items,
    }

    return render(request, "basketapp/basket.html", content)


@login_required
def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if "login" in request.META.get("HTTP_REFERER"):
        return HttpResponseRedirect(reverse("products:product", args=[pk]))

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required
def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_basket_item = Basket.objects.get(pk=int(pk))

        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()

    basket_items = Basket.objects.filter(user=request.user).order_by(
        "product__category"
    )

    content = {
        "basket_items": basket_items,
    }

    result = render_to_string("basketapp/include/inc_basket_list.html", content)
    return JsonResponse({"result": result})


@receiver(pre_save, sender=OrderItem)
@receiver(pre_save, sender=Basket)
def product_quantity_update_save(sender, update_fields, instance, **kwargs):
    if update_fields is "quantity" or "product":
        if instance.pk:
            instance.product.quantity -= (
                instance.quantity - sender.get_item(instance.pk).quantity
            )
        else:
            instance.product.quantity -= instance.quantity
        instance.product.save()


@receiver(pre_delete, sender=OrderItem)
@receiver(pre_delete, sender=Basket)
def product_quantity_update_delete(sender, instance, **kwargs):
    instance.product.quantity += instance.quantity
    instance.product.save()
