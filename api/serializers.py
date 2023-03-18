from rest_framework import serializers
from blog.models import Post

class PostSerializers(serializers.ModelSerializer):
    author = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    authors = serializers.CharField(source='author', read_only = True)
    dates = serializers.DateTimeField(source = 'date', read_only=True, format='%d-%m-%Y')
    class Meta:
        model = Post
        fields = ['title','authors','body','image','dates','author']

class PostCreateSerializers(serializers.ModelSerializer):
    author = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    #authors = serializers.CharField(source='author', read_only = True)
    #dates = serializers.DateTimeField(source = 'date', read_only=True, format='%d-%m-%Y')
    class Meta:
        model = Post
        fields = ['title','body','image','author']