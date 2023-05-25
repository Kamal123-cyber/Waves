from django.db import models

class Donations(models.Model):
    name = models.CharField(max_length=200)
    amount = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name