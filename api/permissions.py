from django.contrib.auth import get_user_model
from rest_framework import permissions

User = get_user_model()

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to perform certain actions.
    """
    user_field = 'user'
    def has_object_permission(self, request, view, obj):
        """
        Check if the user is the owner of the object.
        """
        # If the request method is safe (GET, HEAD, OPTIONS), allow access.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if isinstance(obj, User):
            return obj.id == request.user.id

        if hasattr(obj, self.user_field):
            user = getattr(obj, self.user_field)
            return user == request.user
            # Return whether the object's owner matches the current user.
        return False