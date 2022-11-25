from django.urls import include, path
from rest_framework import routers

from .views import (get_user_token,
                    user_sing_up
                    )

app_name = 'users'

urlpatterns = [
    path('v1/auth/signup/', user_sing_up, name='auth_signup'),
    path('v1/auth/token/', get_user_token, name='auth_token')
]