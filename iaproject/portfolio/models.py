from django.db import models
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.title}'

class Project(models.Model):
    category = models.ForeignKey('Category', null=True, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    image_portrait = models.ImageField(default='project_portrait_default.jpg', upload_to="project_images")
    image_landscape = models.ImageField(default='project_landscape_default.jpg', upload_to="project_images")
    # Added defaults to prevent error if missing image in template
    content = models.TextField()
    order = models.IntegerField(null=True, blank=True)
    home = models.BooleanField(default=False)
    exclude = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

class Section(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=500, blank=True)
    image = models.ImageField(blank=True, upload_to="project_images")
    caption = models.CharField(max_length=200, blank=True)
    caption_url = models.URLField(max_length=200, blank=True)
    content = models.TextField()
    exclude = models.BooleanField(default=False)
    #related names https://simpleisbetterthancomplex.com/tips/2018/02/10/django-tip-22-designing-better-models.html#naming-your-models

class Download(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='downloads')
    title = models.CharField(max_length=500, blank=True)
    content = models.TextField()
    download = models.FileField(upload_to="project_downloads")
    price = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2) #some pdfs are free
    exclude = models.BooleanField(default=False)

    def __str__(self):
        return f'ID {self.id}: {self.title}'