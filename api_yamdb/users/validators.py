from rest_framework import serializers


def user_not_me(value):
    if value.casefold() == 'me':
        raise serializers.ValidationError(
            "Вы не можете создать пользователя  таким username."
        )
    return value
