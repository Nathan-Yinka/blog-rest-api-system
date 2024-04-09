from rest_framework import permissions
from django.contrib.auth import get_user_model

User = get_user_model()


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    
    user_field = "user"

    def has_object_permission(self, request, view, obj):
    # Read permissions are allowed to any request,
    # so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the object is an instance of the User model
        if isinstance(obj, User):
            # If it's a User object, check if obj.id matches request.user.id
            return obj.id == request.user.id
        else:
            if hasattr(obj, self.user_field):
                # Get the user attribute dynamically using getattr
                obj_user = getattr(obj, self.user_field, None)
                # Check if the object's user matches the request user
                return obj_user == request.user
            