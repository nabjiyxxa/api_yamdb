from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (ReviewViewSet, CommentViewSet, CategoryViewSet,
                    GenreViewSet, TitleViewSet)
from users.views import (get_user_token, user_sing_up, UserViewSet)


router_v1 = DefaultRouter()
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register('users', UserViewSet, basename="users")


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', user_sing_up, name='auth_signup'),
    path('v1/auth/token/', get_user_token, name='auth_token'),
    path('v1/', include(router_v1.urls)),
]
