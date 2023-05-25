from django.db import models

# Create your models here.

class StripePayment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    billing_address = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    stripe_session_id = models.CharField(max_length=100)
    status = models.CharField(max_length=10, default='PENDING')

    def __str__(self) -> str:
        return self.name