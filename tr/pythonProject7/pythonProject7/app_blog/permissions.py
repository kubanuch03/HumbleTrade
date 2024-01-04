from rest_framework import permissions


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class IsModeratorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read-only permission for non-moderator users
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow write permissions for moderators
        return request.user.is_staff
