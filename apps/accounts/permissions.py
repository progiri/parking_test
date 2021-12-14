from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 1

class IsManagerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        print(request.user.role)
        return bool(
            request.user.role == 1 or
            request.method in SAFE_METHODS
        )