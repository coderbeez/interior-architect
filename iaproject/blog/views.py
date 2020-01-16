from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Blog, Section, Comment

# Create your views here.
def blogs(request):
    blogs = Blog.objects.filter(exclude=False).order_by('order')
    context = {'blogs': blogs}
    return render(request, 'blog/blogs.html', context)

def blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    sections = Section.objects.filter(blog=blog)
    comments = Comment.objects.filter(blog=blog)
    context = {'blog': blog, 'sections': sections, 'comments': comments}
    return render(request, 'blog/blog.html', context)