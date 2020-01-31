from django.db import models
from django.utils import timezone
from portfolio.models import Project

# Create your models here.
class Role(models.Model):
    company = models.CharField(max_length=200)
    link = models.URLField(max_length=200, blank=True)
    title = models.CharField(max_length=200)
    timeframe = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    order = models.IntegerField(null=True, blank=True)
    job = models.BooleanField(default=False)

    def __str__(self):
        return f'Name: {self.company} {self.title}, ID: {self.id}'
        #name shown in admin

class Point(models.Model):
    role = models.ForeignKey('Role', on_delete=models.CASCADE, related_name='points')
    content = models.TextField()

class Example(models.Model):
    role = models.ForeignKey('Role', on_delete=models.CASCADE, related_name='examples')  
    project = models.ForeignKey('portfolio.Project', on_delete=models.CASCADE, related_name='cv_examples')
    order = models.IntegerField()    


    #related names https://simpleisbetterthancomplex.com/tips/2018/02/10/django-tip-22-designing-better-models.html#naming-your-models


class Skill(models.Model):
    program = models.CharField(max_length=50)
    percent = models.DecimalField(max_digits=3, decimal_places=2) 
    def __str__(self):
        return f'{self.program} {self.percent}'
        #name shown in admin


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

