from rest_framework import permissions


class IsUserOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj) -> bool:

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user


class IsAdminUser(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj) -> bool:
        return request.user.is_admin


class IsSellerUser(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj) -> bool:
        return request.user.is_seller

