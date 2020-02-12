from django.shortcuts import render
#from django.http import HttpResponse
from portfolio.models import Project
from blog.models import Category, Blog

# Create your views here.
def index(request):
    projects = Project.objects.filter(exclude=False, home=True).order_by('order')[:3]
    blogs = Blog.objects.filter(exclude=False).order_by('like')[:3]
    context = {'title': 'Home', 'projects': projects, 'blogs': blogs}
    return render(request, 'home/index.html', context)
    # https://stackoverflow.com/questions/6574003/django-limiting-query-results

