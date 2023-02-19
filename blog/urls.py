from django.urls import path
from .views import (BlogDeleteView, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView)
from . import views
urlpatterns = [
    path('', views.Home , name='home'),
    path('post/', BlogListView.as_view(), name = 'post-home'),
    path('post/<int:pk>/', BlogDetailView.as_view(template_name = 'blog/post-detail.html'), name = 'home-detail'),
    path('post/new/', BlogCreateView.as_view(), name='post-new'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name = 'update'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name="post-delete"),
    path('about/', views.About, name = 'about'),
]
