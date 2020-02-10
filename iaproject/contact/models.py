from django.db import models
from django.utils import timezone


# Create your models here.
class Contact(models.Model):
    ARCHITECTURE = 'Architecture'
    INTERIOR_DESIGN = 'Interior Design'
    GRAPHICS = 'Graphics'
    OTHER = 'Other'

    CATEGORY_CHOICES = [
        (ARCHITECTURE, 'Architecture'),
        (INTERIOR_DESIGN, 'Interior Design'),
        (GRAPHICS, 'Graphics'),
        (OTHER, 'Other'),
    ]
    date = models.DateField(default=timezone.now)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default=OTHER,
    )
# from django docs 
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=200, blank=True)
    query = models.TextField()
    reply = models.TextField(blank=True)

