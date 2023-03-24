from django.urls import path
from .views import SignUpView
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', views.Profile, name='profile'),
    path('password_change/', views.password_change, name='password_change'),
     
]
