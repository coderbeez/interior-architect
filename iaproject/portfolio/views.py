from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Category, Project, Section, Download

def projects(request):
    project_list = Project.objects.filter(exclude=False).order_by('order')
    paginator = Paginator(project_list, 3) # Show 3 blogs per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'title': 'Portfolio', 'page_obj': page_obj}
    return render(request, 'portfolio/projects.html', context)
    # pagination from django docs https://docs.djangoproject.com/en/3.0/topics/pagination/

def project(request, pk):
    project = Project.objects.get(pk=pk)
    sections = Section.objects.filter(project=project)
    downloads = Download.objects.filter(exclude=False, project=project)
    context = {'title': 'Portfolio', 'project': project, 'sections': sections, 'downloads': downloads}
    return render(request, 'portfolio/project.html', context)