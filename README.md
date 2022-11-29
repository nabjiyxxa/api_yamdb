# API Yamdb

API для проекта Yamdb.
Проект позволяет оставлять отзывы на произведения различных жанров(музыка. фильмы итд). Есть возможность ставить рейтинг. Налажена возможность регистрации и авторизации

Требования
----------
* Python 3.8+


Установка 
----------


1. Cоздать и активировать виртуальное окружение:
```bash
python3 -m venv env

source env/bin/activate
```
2. Установить зависимости из файла ```requirements.txt```:
```bash
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```
3. Выполнить миграции:
```bash
cd api_yamdb

python3 manage.py migrate
```
4. Запустить проект:
```bash
python3 manage.py runserver
```
