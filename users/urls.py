from django.urls import path
from .views import SignUpView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', views.Profile, name='profile'),
]
