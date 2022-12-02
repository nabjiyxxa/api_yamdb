from rest_framework import serializers

from .models import User
from .validators import user_not_me


class UserSingUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username')

    def validate_username(self, value):
        return user_not_me(value)


class TokenSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=150)
    confirmation_code = serializers.CharField(max_length=6)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )

    def validate_username(self, value):
        return user_not_me(value)
