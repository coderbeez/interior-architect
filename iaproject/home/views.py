from django.shortcuts import render
from blog.models import Blog
from portfolio.models import Project

def index(request):
    '''Render the home page.
    Include 3 projects where the home field is True, order by order field. 
    Include the 3 most liked blogs, most liked first.
    Credit: https://stackoverflow.com/questions/6574003/django-limiting-query-results'''
    projects = Project.objects.filter(exclude=False, home=True).order_by('order')[:3]
    blogs = Blog.objects.filter(exclude=False).order_by('-like')[:3]
    context = {'title': 'Home', 'projects': projects, 'blogs': blogs}
    return render(request, 'home/index.html', context)