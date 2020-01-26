from django.db import models
from portfolio.models import Project

# Create your models here.
class Role(models.Model):
    company = models.CharField(max_length=200)
    link = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200)
    timeframe = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return f'<Name: {self.company} {self.title}, ID: {self.id}>'
        #name shown in admin

class Point(models.Model):
    role = models.ForeignKey('Role', on_delete=models.CASCADE, related_name='points')
    content = models.TextField()

class Example(models.Model):
    role = models.ForeignKey('Role', on_delete=models.CASCADE, related_name='examples')  
    project = models.ForeignKey('portfolio.Project', on_delete=models.CASCADE, related_name='examples')
    order = models.IntegerField()    


    #related names https://simpleisbetterthancomplex.com/tips/2018/02/10/django-tip-22-designing-better-models.html#naming-your-models


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

