from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializers, PostCreateSerializers
from blog.models import Post
# Create your views here.

class PostApiView(generics.ListAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()

class PostDetailApiView(generics.RetrieveAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()

class PostCreateApiView(generics.CreateAPIView):
    serializer_class = PostCreateSerializers
    queryset = Post.objects.all()
    
    def perform_create(self, serializer):
        serializer.save()


   