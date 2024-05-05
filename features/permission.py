from rest_framework import permissions


class AccessPermission(permissions.BasePermission):
    message = 'You are not a manager'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return False


class StoryPermission(permissions.BasePermission):
    message = 'You are not a manager'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.user == request.user


class StoryCommentPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.user == request.user
