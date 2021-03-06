from django.shortcuts import render
from app.models import Post  , Category
from app.serializer import PostSerializer ,AuthorSerializer, CategorySerializer
from rest_framework import generics,serializers  


class PostList(generics.ListCreateAPIView):  
    queryset = Post.objects.all()  
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):  
    queryset = Post.objects.all()  
    serializer_class = PostSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer