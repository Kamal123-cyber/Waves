from django.urls import path
from . import views
urlpatterns = [
    path('pay/', views.Pay, name='pay')
]
