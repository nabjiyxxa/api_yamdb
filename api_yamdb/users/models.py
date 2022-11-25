from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models


class User(AbstractUser):

    ROLE_USER = 'user'
    ROLE_MODERATOR = 'moderator'
    ROLE_ADMIN = 'admin'

    ROLE_CHOICES = (
        (ROLE_USER, 'Пользователь'),
        (ROLE_MODERATOR, 'Модератор'),
        (ROLE_ADMIN, 'Админ'),
    )

    bio = models.TextField(
        max_length=300,
        blank=True,
        verbose_name='Подробности'
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Электронная почта'
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=ROLE_USER,
        verbose_name='Роль'
    )
    confirmation_code = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Код для авторизации'
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_user'
            )
        ]
