from django.db import models

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


    #related names https://simpleisbetterthancomplex.com/tips/2018/02/10/django-tip-22-designing-better-models.html#naming-your-models
