from django.db import models
from django.utils import timezone


class Contact(models.Model):
    '''Indivdual visitor contact and admin reply.
    Credit: Choice fields
    https://stackoverflow.com/questions/18676156/how-to-properly-use-the-choices-field-option-in-django
    '''
    ARCHITECTURE = 'Architecture'
    GRAPHICS = 'Graphics'
    INTERIOR_DESIGN = 'Interior Design'
    GENERAL = 'General'

    CATEGORY_CHOICES = [
        (ARCHITECTURE, 'Architecture'),
        (GRAPHICS, 'Graphics'),
        (INTERIOR_DESIGN, 'Interior Design'),
        (GENERAL, 'General'),
    ]

    date = models.DateField(default=timezone.now)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
    )
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=200, blank=True)
    query = models.TextField()
    reply = models.TextField(blank=True)
    exclude = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'
