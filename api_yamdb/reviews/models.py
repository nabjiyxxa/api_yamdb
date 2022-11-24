from django.db import models
from datetime import datetime

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
        validators=[datetime.now().year]
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