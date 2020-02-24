from django.db import models
from django.utils import timezone
from portfolio.models import Download

class Cart(models.Model):
    date = models.DateField(default=timezone.now) # auto
    downloads = models.ManyToManyField(Download, blank=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    stripe = models.CharField(max_length=200, blank=True)
    fulfilled = models.BooleanField(default=False)

    def __str__(self):
        return f'Cart {self.id} {self.date}'
