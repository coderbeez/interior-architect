from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Project, Section, Download

def projects(request):
    '''Renders an ordered list of projects on portfolio page.
    Paginates after every 6 projects.
    Credit: Pagination https://docs.djangoproject.com/en/3.0/topics/pagination/ '''
    project_list = Project.objects.filter(exclude=False).order_by('order')
    paginator = Paginator(project_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'title': 'Portfolio', 'page_obj': page_obj}
    return render(request, 'portfolio/projects.html', context)

def project(request, pk):
    '''Renders an individual project, its sections and downloads, on project page.'''
    project = get_object_or_404(Project, pk=pk)
    sections = Section.objects.filter(project=project).order_by('id')
    downloads = Download.objects.filter(exclude=False, project=project)
    context = {'title': 'Portfolio', 'project': project, 'sections': sections, 'downloads': downloads}
    return render(request, 'portfolio/project.html', context)