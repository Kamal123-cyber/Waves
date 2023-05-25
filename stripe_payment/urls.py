from django.urls import path
from .views import payment_view, payment_success_view, payment_cancel_view

urlpatterns = [
                path('payment/', payment_view, name='payment_view'),
                path('payment/success/', payment_success_view, name='payment_success'),
                path('payment/cancel/', payment_cancel_view, name='payment_cancel'),
            ]