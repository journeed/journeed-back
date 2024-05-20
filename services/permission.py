from rest_framework import permissions
from partnership.models import RentCar


class ManagerPermission(permissions.BasePermission):
    message = 'You are not a manager'

    def has_permission(self, request, view):
        return request.user.is_superuser


class ManagerObjectPermission(permissions.BasePermission):
    message = 'You are not a manager'

    def has_permission(self, request, view):
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.user == request.user


class ObjectPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.user == request.user


class CarsPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if RentCar.objects.filter(user=request.user):
            return True
        return request.user.is_partnership

    def has_object_permission(self, request, view, obj):
        if RentCar.objects.filter(user=request.user):
            return True
        return obj.user == request.user


class CarReviewPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

