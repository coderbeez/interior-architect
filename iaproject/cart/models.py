from django.db import models
from portfolio.models import Download

# Create your models here.

class Cart(models.Model):
    downloads = models.ManyToManyField(Download, blank=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    #credit https://www.youtube.com/watch?v=20HCDEwEdeo&list=PLPp4GCMxKSjCM9AvhmF9OHyyaJsN8rsZK&index=23&t=0s



