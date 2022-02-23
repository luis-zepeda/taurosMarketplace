from rest_framework import permissions


class IsProductOwner(permissions.BasePermission):
    """Allow access only to products owned by the requesting user."""

    def has_object_permission(self, request, view, obj) ->bool:
        print(request.user)
        print(obj.owner)
        return request.user == obj.owner
