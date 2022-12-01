import csv

from django.core.management.base import BaseCommand, CommandError

from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User


ThroughModel = Title.genre.through

PATH = 'static/data'
KEY_FIELDS = ('category', 'author')
DICT_MODEL = {
    User: 'users.csv',
    Genre: 'genre.csv',
    Category: 'category.csv',
    Title: 'titles.csv',
    Review: 'review.csv',
    Comment: 'comments.csv',
    ThroughModel: 'genre_title.csv'
}


def csv_writer(csv_data, model):
    objs = list()
    for row in csv_data:
        for field in KEY_FIELDS:
            if field in row:
                row[f'{field}_id'] = row[field]
                del row[field]
        objs.append(model(**row))
    model.objects.bulk_create(objs)


class Command(BaseCommand):
    help = 'Импорт в базу тестовых данных из файлов'

    def handle(self, *args, **options):
        for model in DICT_MODEL:
            try:
                with open(
                    PATH + DICT_MODEL[model],
                    newline='',
                    encoding='utf8'
                ) as csv_file:
                    csv_writer(csv.DictReader(csv_file), model)
            except Exception as error:
                CommandError(error)
            self.stdout.write(f'Файл импортирован. Модель: {model}')
