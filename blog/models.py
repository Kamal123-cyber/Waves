from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=32)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('home-detail', args=[str(self.pk)])

class Comment(models.Model):
    comm = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

   
