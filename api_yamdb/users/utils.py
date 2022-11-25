from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from .models import User
import random

from api_yamdb.settings import EMAIL_SERVER


def generate_confirmation_code(username):
    user = get_object_or_404(User, username=username)
    confirmation_code = str(random.randint(100000, 999999))
    user.confirmation_code = confirmation_code
    send_mail(
        f'Code for registrations',
        f'Код для получения JWT токена {user.confirmation_code}',
        EMAIL_SERVER,
        [user.email],
        fail_silently=False,
    )
    user.save()
