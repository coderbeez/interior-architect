from django.db import models
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    image = models.ImageField(blank=True)
    content = models.TextField()

    def __str__(self):
        return f'<Name: {self.title}, ID: {self.id}>'
        #name shown in admin

class Section(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=500)
    image = models.ImageField(blank=True)
    content = models.TextField()

class Comment(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()

    #related names https://simpleisbetterthancomplex.com/tips/2018/02/10/django-tip-22-designing-better-models.html#naming-your-models




