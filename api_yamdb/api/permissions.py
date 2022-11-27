from rest_framework import permissions


class IsAuthorOrModeratorOrAdminPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or (request.user.is_authenticated and (
                request.user.is_admin
                or request.user.is_moderator)
                )
        )


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or (
                request.user.is_authenticated
                and request.user.is_admin)
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or (
                request.user.is_authenticated
                and request.user.is_admin)
        )


class IsAdminPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
                request.user.is_authenticated
                and request.user.is_admin
        )


class IsUserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated
