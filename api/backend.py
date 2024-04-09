from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework.authentication import TokenAuthentication as BaseTokenAuth

User = get_user_model()

class EmailModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            pass
        return None

class TokenAuthentication(BaseTokenAuth):
    keyword = "Bearer"