from django.core.exceptions import ValidationError
from django.utils import timezone

CREATION_YEAR = 1739


def validate_year(value):
    """
    Валидатор для проверки года
    """
    year_now = timezone.now().year
    if year_now >= value >= CREATION_YEAR:
        return value
    else:
        raise ValidationError(
            f'Год выпуска произведения {value} не может быть позже '
            f'настоящего года {year_now}, и раньше даты '
            f'создания произведения "{CREATION_YEAR}"г.'
        )
