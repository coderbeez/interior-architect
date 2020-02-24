from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Category, Blog, Section, Comment
from .forms import CommentForm, ReplyForm

def blogs(request):
    blog_list = Blog.objects.filter(exclude=False).order_by('order')
    paginator = Paginator(blog_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'title': 'Blog', 'page_obj': page_obj}
    return render(request, 'blog/blogs.html', context)
    # pagination from django docs https://docs.djangoproject.com/en/3.0/topics/pagination/

def blog(request, pk):
    #blog = Blog.objects.get(pk=pk)
    blog = get_object_or_404(Blog, pk=pk)
    sections = Section.objects.filter(blog=blog).order_by('id')
    comments = Comment.objects.filter(exclude=False, blog=blog).order_by('-id')
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment (
                blog = blog,
                content = form.cleaned_data['content']
            )
            comment.save()
            messages.success(request, f'Thanks for your comment!')
            return redirect('blog', pk=pk)
        else:
            messages.error(request, f'Something went wrong - comment not posted!')       
    context = {'title': 'Blog', 'blog': blog, 'sections': sections, 'comments': comments, 'form': form}    
    return render(request, 'blog/blog.html', context)
    #redirect to avoid resubmission problems
    #might not need an else as django creates validation errors?
    #add real python credit
    #credit: https://stackoverflow.com/questions/3209906/django-return-redirect-with-parameters

def like(request, pk):
    #blog = Blog.objects.get(pk=pk)
    blog = get_object_or_404(Blog, pk=pk)
    blog.like += 1
    blog.save()
    messages.success(request, f'Thanks for liking this blog!')
    return redirect('blog', pk=pk)
    #Credit: https://stackoverflow.com/questions/36479776/adding-vote-buttons-to-django-objects
  
@login_required
def comments(request, pk=None):
    '''order by oldest without reply'''
    comments = Comment.objects.filter(exclude=False, reply='').order_by('id')
    form = ReplyForm()  
    if request.method == 'POST':
        #comment = Comment.objects.get(pk=pk)
        comment = get_object_or_404(Comment, pk=pk)
        form = ReplyForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            if comment.exclude:
                messages.success(request, f'Comment excluded!')
            elif comment.reply !='':
                messages.success(request, f'Comment reply posted!')
            else:
                messages.warning(request, 'No change saved.')    
            return redirect('comments')
        else:
            messages.error(request, f'Something went wrong!')   
    context = {'title': 'Comments', 'comments': comments, 'form': form}
    return render(request, 'blog/comments.html', context)
    #Credit: https://stackoverflow.com/questions/38046905/sending-post-data-from-inside-a-django-template-for-loop
    #What should the else do?