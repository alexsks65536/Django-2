from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta
from django.utils.timezone import now


"""
Возвращает время действия ключа пользователя
"""


def default_key_expiration_date():
    return timezone.now() + timedelta(hours=48)


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to="users_avatars", blank=True)
    age = models.PositiveIntegerField(verbose_name="возраст")
    activation_key = models.CharField(
        verbose_name="Ключ активации", max_length=128, blank=True
    )
    activation_key_expires = models.DateTimeField(
        verbose_name="Активация истекает", default=default_key_expiration_date
    )

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True
