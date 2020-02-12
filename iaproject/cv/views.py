from django.shortcuts import render
from django.contrib import messages
from .models import Role, Point, Example, Skill

def about(request):
    jobs = Role.objects.filter(job=True).order_by('-order')
    studies = Role.objects.filter(job=False).order_by('-order')
    skills = Skill.objects.all()
    context = {'title': 'About', 'jobs': jobs, 'studies': studies, 'skills': skills}
    return render(request, 'cv/about.html', context)