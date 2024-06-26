from django.shortcuts import render,get_object_or_404
from .serializers import BlogPostSerializer,CaterorySerializer
from rest_framework import generics,status
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import BlogPost,Category
from api.permissions import IsOwnerOrReadOnly as BaseIsOwnerOrReadOnly

class IsOwnerOrReadOnly(BaseIsOwnerOrReadOnly):
    user_field = "author"

class BlogPostUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
class UserBlogPostListView(generics.ListAPIView):
    serializer_class = BlogPostSerializer
    
    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        user = get_object_or_404(User,id=user_id)
        
        qs = user.user_posts.all()
        return qs
        
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CaterorySerializer
    
class CateroryBlogListView(generics.ListAPIView):
    serializer_class = BlogPostSerializer
    
    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        category = get_object_or_404(Category, id=category_id)
        qs = category.caterory_blogs.all()
        
        return qs
    
    
