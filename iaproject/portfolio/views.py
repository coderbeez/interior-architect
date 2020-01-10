from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Section

# Create your views here.
def projects(request):
    #return HttpResponse('Portfolio List')
    projects = Project.objects.all().order_by('-date')
    context = {'projects': projects}
    return render(request, 'portfolio/projects.html', context)

def project(request, pk):
    project = Project.objects.get(pk=pk)
    sections = Section.objects.filter(project=project)
    context = {'project': project, 'sections': sections}
    return render(request, 'portfolio/project.html', context)

