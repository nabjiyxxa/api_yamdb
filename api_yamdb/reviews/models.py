from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from users.models import User


class Review(models.Model):
    MESSAGE_FORM = (
        'Дата публикации: {}, '
        'автор: {}, '
        'произведение: {}, '
        'отзыв: {:.15}'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор отзыва'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение'
    )
    text = models.TextField()
    score = models.IntegerField(
        'Оценка (от 1 до 10)',
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.MESSAGE_FORM.format(
            self.pub_date,
            self.author.username,
            self.title,
            self.text
        )
