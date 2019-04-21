from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
        Check if user is admin or owner of the resource.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj.owner == request.user