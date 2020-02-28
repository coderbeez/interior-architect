from django.shortcuts import render
from blog.models import Blog
from portfolio.models import Project


def index(request):
    '''Renders the home page.
    Includes 3 projects and 3 blogs.
    Credit: Limiting results
    https://stackoverflow.com/questions/6574003/django-limiting-query-results
    '''
    projects = Project.objects.filter(
        exclude=False, home=True
    ).order_by('order')[:3]
    blogs = Blog.objects.filter(exclude=False).order_by('-like')[:3]
    context = {'title': 'Home', 'projects': projects, 'blogs': blogs}
    return render(request, 'home/index.html', context)
