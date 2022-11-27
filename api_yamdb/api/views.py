from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from reviews.models import Title, Review, Category, Genre

from .serializers import (ReviewSerializer, CommentSerializer,
                          TitleReadSerializer, TitleWriteSerializer,
                          CategorySerializer, GenreSerializer)
from .permissions import (IsAuthorAdminModeratorOrReadOnly,
                          IsAdminOrReadOnly, IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthorOrReadOnly)
    search_fields = ('=name')
    lookup_field = 'slug'
    # pagination_class = 10


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthorOrReadOnly)
    search_fields = ('=name')
    lookup_field = 'slug'
    # pagination_class = 10

    # def retrieve(self, request, *args, **kwargs):
    #    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class TitleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Title.objects.all().annotate(rating=Avg('reviews__score'))

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return TitleReadSerializer
        return TitleWriteSerializer


# class TitleViewSet(viewsets.ModelViewSet):
#     queryset = Title.objects.all()
#     permission_classes = (IsAuthorOrReadOnly)
#     serializer_class = TitleSerializer
#     # pagination_class = 10

#     def update(self, request, *args, **kwargs):
#         return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsAuthorAdminModeratorOrReadOnly
    )

    def get_title(self):
        return get_object_or_404(
            Title,
            pk=self.kwargs.get('title_id')
        )

    def get_queryset(self):
        return self.get_title().reviews.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            title=self.get_title()
        )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsAuthorAdminModeratorOrReadOnly
    )

    def get_review(self):
        return get_object_or_404(
            Review,
            pk=self.kwargs.get('review_id'),
            title_id=self.kwargs.get('title_id')
        )

    def get_queryset(self):
        return self.get_review().comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            review=self.get_review()
        )
