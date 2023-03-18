from django.urls import path
from .views import PostApiView, PostCreateApiView, PostDetailApiView
urlpatterns = [
    path('postapi/', PostApiView.as_view()),
    path('postapi/<int:pk>/', PostDetailApiView.as_view()),
    path('post/create_api/', PostCreateApiView.as_view())
]