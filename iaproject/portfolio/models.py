from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return f'<Name: {self.title}>'
        #name shown in admin

class Project(models.Model):
    category = models.ForeignKey('Category', null=True, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    image_portrait = models.ImageField(blank=True)
    image_landscape = models.ImageField(blank=True)
    content = models.TextField()
    order = models.IntegerField(null=True)

    def __str__(self):
        return f'<Order: {self.order}, Name: {self.title}, ID: {self.id}>'
        #name shown in admin

class Section(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='sections')
    image_portrait = models.ImageField(blank=True)
    image_landscape = models.ImageField(blank=True)
    content = models.TextField()


    #related names https://simpleisbetterthancomplex.com/tips/2018/02/10/django-tip-22-designing-better-models.html#naming-your-models

