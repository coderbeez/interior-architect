from django.db import models
from django.utils import timezone

class Category(models.Model):
    '''Blog category list item.'''
    title = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.title}'

class Blog(models.Model):
    '''Individual blog and header data.'''
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='blogs') # no null !!!
    title = models.CharField(max_length=50) # char blank - no blank
    date = models.DateField(default=timezone.now) # auto
    image = models.ImageField(default='blog_default.jpg', upload_to='blog_images') # image blank
    content = models.TextField(blank=True) # text blank
    order = models.IntegerField(null=True, blank=True) # null ok - should not be required in form!!!
    like = models.IntegerField(default=0)
    exclude = models.BooleanField(default=False) # yes no

    def __str__(self):
        return f'{self.title}'

class Section(models.Model):
    '''Section data for an individual blog.
    Fields set to blank=True allow for maximum flexibility.'''
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=500, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='blog_images')
    caption = models.CharField(max_length=200, blank=True)
    caption_url = models.URLField(max_length=200, blank=True)
    exclude = models.BooleanField(default=False)

class Comment(models.Model):
    '''Visitor comment and admin reply for an individual blog.'''
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='comments')
    date = models.DateField(default=timezone.now)
    content = models.TextField()
    reply = models.TextField(blank=True)
    exclude = models.BooleanField(default=False)  
    # Credit: Related names https://simpleisbetterthancomplex.com/tips/2018/02/10/django-tip-22-designing-better-models.html#naming-your-models




