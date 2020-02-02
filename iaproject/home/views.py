from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Category, Blog

# Create your views here.
def index(request):
    #return HttpResponse('Home')

    blogs = Blog.objects.filter(exclude=False).order_by('order')[:3]
    context = {'title': 'Home', 'blogs': blogs}




    return render(request, 'home/index.html', context)
    # https://stackoverflow.com/questions/6574003/django-limiting-query-results

