from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

from datetime import datetime

from django.conf import settings


CREATION_YEAR = 1739


def validate_year(value):
    """
    Валидатор для проверки года
    """
    year_now = datetime.now().year
    if year_now >= value >= CREATION_YEAR:
        return value
    else:
        raise ValidationError(
            f'Год выпуска произведения {value} не может быть позже '
            f'настоящего года {year_now}, и раньше даты '
            f'создания произведения "{CREATION_YEAR}"г.'
        )


class Category(models.Model):
    name = models.CharField(
        'Категория',
        max_length=256,
    )
    slug = models.SlugField('Категория слаг', unique=True, max_length=50)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        'Жанр',
        max_length=256,
    )
    slug = models.SlugField('Жанр слаг', unique=True, max_length=50)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        'Название произведения',
        max_length=256
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
        Category,
        on_delete=models.SET_NULL,
        related_name='category',
        null=True,
        blank=True,
        verbose_name='Категория произведения'
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        related_name='genres',
        verbose_name='Жанр'
    )

    class Meta:
        verbose_name = "Произведение"
        verbose_name_plural = "Произведения"

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    """
    Реализована связь МКМ.
    """
    genre = models.ForeignKey(
        Genre,
        related_name='genretitle',
        on_delete=models.CASCADE,
        verbose_name='Жанр'
    )
    title = models.ForeignKey(
        Title,
        related_name='genretitle',
        on_delete=models.CASCADE,
        verbose_name='Произведение'
    )

    def __str__(self):
        return f'{self.genre.name} {self.title.name}'


class Review(models.Model):
    MESSAGE_FORM = (
        'Дата публикации: {}, '
        'автор: {}, '
        'произведение: {}, '
        'отзыв: {:.15}'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
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
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_author_title'
            )
        ]

    def __str__(self):
        return self.MESSAGE_FORM.format(
            self.pub_date,
            self.author.username,
            self.title,
            self.text
        )


class Comment(models.Model):
    MESSAGE_FORM = (
        'Дата публикации: {}, '
        'автор: {}, '
        'отзыв: {}, '
        'комментарий: {:.15}'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.MESSAGE_FORM.format(
            self.pub_date,
            self.author.username,
            self.review,
            self.text
        )
