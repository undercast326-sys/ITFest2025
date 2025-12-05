from rest_framework import permissions


class IsModeratorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.groups.filter(name__in=['moderator']).exists():
            return True

        return False