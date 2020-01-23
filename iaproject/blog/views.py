from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category, Blog, Section, Comment
from .forms import CommentForm

# Create your views here.
def blogs(request):
    blogs = Blog.objects.filter(exclude=False).order_by('order')
    context = {'blogs': blogs}
    return render(request, 'blog/blogs.html', context)

def blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    sections = Section.objects.filter(blog=blog)
    comments = Comment.objects.filter(blog=blog)
    form = CommentForm()
    context = {'blog': blog, 'sections': sections, 'comments': comments, 'form': form}
    
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment (
                blog = blog,
                content = form.cleaned_data['content']
            )
            comment.save()
            messages.success(request, f'Comment added')
            #return redirect('blog')
            #esle form is not valid??? only thing that could be would be empty contents?
        

    return render(request, 'blog/blog.html', context)