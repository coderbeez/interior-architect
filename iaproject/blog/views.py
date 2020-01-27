from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Category, Blog, Section, Comment
from .forms import CommentForm

# Create your views here.
def blogs(request):
    blog_list = Blog.objects.filter(exclude=False).order_by('order')
    paginator = Paginator(blog_list, 3) # Show 3 blogs per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/blogs.html', {'page_obj': page_obj})
    # pagination from django docs https://docs.djangoproject.com/en/3.0/topics/pagination/


def blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    sections = Section.objects.filter(blog=blog)
    comments = Comment.objects.filter(blog=blog).order_by('-id')
    form = CommentForm() #equate to request.GET
    
    if request.method == 'POST':
        form = CommentForm(request.POST) #tried instance=blog and blog=blog
        if form.is_valid():
            comment = Comment (
                blog = blog,
                content = form.cleaned_data['content']
            )
            comment.save()
            #from printout... think there should be a cleaner way to do this
            messages.success(request, f'Thanks for your comment!')
            #form = CommentForm() don't need with redirect
            return redirect('blog', pk=pk)
            #redirect to avoid resubmission problems - ask Paul/Google
            #might not need an else as django creates validation errors???
            #credit: https://stackoverflow.com/questions/3209906/django-return-redirect-with-parameters

    context = {'blog': blog, 'sections': sections, 'comments': comments, 'form': form}    

    return render(request, 'blog/blog.html', context)