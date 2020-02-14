from django.db import models
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.title}'

class Blog(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='blogs') # no null !!!
    title = models.CharField(max_length=50) # char blank - no blank
    date = models.DateField(default=timezone.now) # auto
    image = models.ImageField(default='blog_default.jpg', upload_to='blog_images') # image blank
    content = models.TextField(blank=True) # text blank
    order = models.IntegerField(null=True, blank=True) # null ok - should not be required in form!!!
    exclude = models.BooleanField(default=False) # yes no
    like = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}'

class Section(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='sections') #gotta have
    title = models.CharField(max_length=500, blank=True) # char blank
    content = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='blog_images') # ?
    caption = models.CharField(max_length=200, blank=True)
    caption_url = models.URLField(max_length=200, blank=True)
    exclude = models.BooleanField(default=False)

class Comment(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='comments')
    date = models.DateField(default=timezone.now)
    content = models.TextField() # don't want this to blank ever
    reply = models.TextField(blank=True)
    exclude = models.BooleanField(default=False)  
 
    #related names https://simpleisbetterthancomplex.com/tips/2018/02/10/django-tip-22-designing-better-models.html#naming-your-models




