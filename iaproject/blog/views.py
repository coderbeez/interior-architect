from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Section, Comment
from .forms import CommentForm, ReplyForm


def blogs(request):
    '''Renders an ordered list of blogs on the blogs page.
    Paginates after every 6 blogs.
    Credit: Pagination
    https://docs.djangoproject.com/en/3.0/topics/pagination/
    '''
    blog_list = Blog.objects.filter(exclude=False).order_by('order')
    paginator = Paginator(blog_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'title': 'Blog', 'page_obj': page_obj}
    return render(request, 'blog/blogs.html', context)


def blog(request, pk):
    '''Renders an individual blog, its sections and comments, on the blog page.
    Renders a comment form.
    Creates an indivdual comment on valid from post.
    Sends email flag on valid form post.
    Credit: Save instance
    https://realpython.com/get-started-with-django-1/
    Credit: Redirect with parameters
    https://stackoverflow.com/questions/3209906/django-return-redirect-with-parameters
    '''
    blog = get_object_or_404(Blog, pk=pk)
    sections = Section.objects.filter(blog=blog).order_by('id')
    comments = Comment.objects.filter(exclude=False, blog=blog).order_by('-id')
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                blog=blog,
                content=form.cleaned_data['content']
            )
            comment.save()
            send_mail(
                'New Comment',
                'You have a new comment.',
                'cos.interior.architect@gmail.com',
                ['sullivanedel@hotmail.com', ],
                fail_silently=False,
            )
            messages.success(request, f'Thanks for your comment!')
            return redirect('blog', pk=pk)
        else:
            messages.error(
                request, f'Something went wrong - comment not posted!')
    context = {'title': 'Blog', 'blog': blog,
               'sections': sections, 'comments': comments, 'form': form}
    return render(request, 'blog/blog.html', context)


def like(request, pk):
    '''Increments like field for an individual blog.
    Credit: Upvoting
    https://stackoverflow.com/questions/36479776/adding-vote-buttons-to-django-objects
    '''
    blog = get_object_or_404(Blog, pk=pk)
    blog.like += 1
    blog.save()
    messages.success(request, f'Thanks for liking this blog!')
    return redirect('blog', pk=pk)


@login_required
def comments(request, pk=None):
    ''' View accessed by site admin only, login required.
    Renders outstanding comments (i.e. not excluded and no reply),
    oldest first, on the comments page.
    Renders reply form for each comment.
    Updates individual comment on valid form post.
    '''
    comments = Comment.objects.filter(exclude=False, reply='').order_by('id')
    form = ReplyForm()
    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=pk)
        form = ReplyForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            if comment.exclude:
                messages.success(request, f'Comment excluded!')
            elif comment.reply != '':
                messages.success(request, f'Comment reply posted!')
            else:
                messages.warning(request, 'No change saved.')
            return redirect('comments')
        else:
            messages.error(request, f'Something went wrong!')
    context = {'title': 'Comments', 'comments': comments, 'form': form}
    return render(request, 'blog/comments.html', context)
