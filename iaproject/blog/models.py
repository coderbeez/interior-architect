from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return f'<Name: {self.title}>'
        #name shown in admin


class Blog(models.Model):
    category = models.ForeignKey('Category', null=True, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=200, blank=True)
    date = models.DateField(default=timezone.now)
    image = models.ImageField(blank=True)
    content = models.TextField(blank=True)
    order = models.IntegerField(null=True)
    exclude = models.BooleanField(default=False)

    def __str__(self):
        return f'<Order: {self.order}, Name: {self.title}, ID: {self.id}>'
        #name shown in admin


class Section(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=500, blank=True)
    image = models.ImageField(blank=True)
    content = models.TextField(blank=True)
    


class Comment(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()

    #related names https://simpleisbetterthancomplex.com/tips/2018/02/10/django-tip-22-designing-better-models.html#naming-your-models




