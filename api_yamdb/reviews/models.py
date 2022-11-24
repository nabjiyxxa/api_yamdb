from django.db import models
from datetime import datetime

from django.core.exceptions import ValidationError


CINEMATOGRAPHY_CREATION_YEAR = 1895

def validate_year(value):
    """
    Валидатор для проверки введенного года выпуска произведения.
    """
    year_now = datetime.now().year
    if year_now >= value >= CINEMATOGRAPHY_CREATION_YEAR:
        return value
    else:
        raise ValidationError(
            f'Год выпуска произведения {value} не может быть больше '
            f'настоящего года {year_now}, либо меньше даты '
            f'создания кинематографа "{CINEMATOGRAPHY_CREATION_YEAR}"г.'
            'Проверьте введеные данные.'
        )

class Title(models.Model):
    # нужен ли primary_key=True
    # id = models.AutoField(primary_key=True)
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
        related_name='genres'
    )

    class Meta:
        #ordering = ['-id'] не id другое 
        verbose_name = "Произведение"
        verbose_name_plural = "Произведения"

    def __str__(self):
        return self.name