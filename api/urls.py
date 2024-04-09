from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls), 
    path("auth/",include("user.urls")),  # the urls for the authentication system
    path("api/",include("blog.urls")), # the urls for the blog system
]
