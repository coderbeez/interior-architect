from django.contrib import messages
from django.shortcuts import render
from .models import Role, Skill

def about(request):
    '''Render about page.
    Include all roles as jobs or studies, depending on job field.
    Include all skills.'''
    jobs = Role.objects.filter(job=True).order_by('-order')
    studies = Role.objects.filter(job=False).order_by('-order')
    skills = Skill.objects.all()
    context = {'title': 'About', 'jobs': jobs, 'studies': studies, 'skills': skills}
    return render(request, 'cv/about.html', context)