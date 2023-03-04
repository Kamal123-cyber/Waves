from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=32)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to='post_file', blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    @property
    def imageURL(self):
        if self.image:
            return self.image.url
        else:
            return None
        
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('home-detail', args=[str(self.pk)])


class comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=20, blank=False)
    body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name


    
   
