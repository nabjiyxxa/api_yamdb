from django.db import models
from datetime import datetime

from django.core.exceptions import ValidationError


CINEMATOGRAPHY_CREATION_YEAR = 1895

def validate_year(value):
    """
    Валидатор для проверки года
    """
    year_now = datetime.now().year
    if year_now >= value >= CINEMATOGRAPHY_CREATION_YEAR:
        return value
    else:
        raise ValidationError(
            f'Год выпуска произведения {value} не может быть позже '
            f'настоящего года {year_now}, и раньше даты '
            f'создания произведение "{CINEMATOGRAPHY_CREATION_YEAR}"г.'
        )

class Title(models.Model):
    name = models.CharField(
        'Название произведения',
        max_length=256,
        unique=True
    )
    year = models.IntegerField(
        'Год выхода',
        validators=[validate_year],
        null=True
    )
    description = models.CharField(
        'Описание',
        max_length=512,
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category, # создам модель категорий
        on_delete=models.SET_NULL,
        related_name='category',
        null=True,
        blank=True,
        verbose_name='Категория произведения'
    )
    genre = models.ManyToManyField(
        Genre, # зе сейм
        blank=True,
        related_name='genres',
        verbose_name='Жанр'
    )

    class Meta:
        #ordering = ['-id'] не id другое 
        verbose_name = "Произведение"
        verbose_name_plural = "Произведения"

    def __str__(self):
        return self.name