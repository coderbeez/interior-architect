from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=20)
    
    def __str__(self):
        return f'<Name: {self.title}>'
        #name shown in admin


class Blog(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='blogs') # no null !!!
    title = models.CharField(max_length=50) # char blank - no blank
    date = models.DateField(default=timezone.now) # auto
    image = models.ImageField(blank=True) # image blank
    content = models.TextField(blank=True) # text blank
    order = models.IntegerField(null=True, blank=True) # null ok - should not be required in form!!!
    exclude = models.BooleanField(default=False) # yes no

    def __str__(self):
        return f'<Order: {self.order}, Name: {self.title}, ID: {self.id}>'
        #name shown in admin


class Section(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='sections') #gotta have
    title = models.CharField(max_length=500, blank=True) # char blank
    image = models.ImageField(blank=True) # ?
    content = models.TextField(blank=True) # text blank
    


class Comment(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='comments')
    date = models.DateField(default=timezone.now)
    name = models.CharField(max_length=30, blank=True)
    content = models.TextField() # don't want this to blank ever
    reply = models.TextField(blank=True)
 

    #related names https://simpleisbetterthancomplex.com/tips/2018/02/10/django-tip-22-designing-better-models.html#naming-your-models




