from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Role, Point, Example, Skill, Contact
from .forms import ContactForm

# Create your views here.

def about(request):
    jobs = Role.objects.filter(job=True).order_by('order')
    studies = Role.objects.filter(job=False).order_by('order')
    skills = Skill.objects.all()
    context = {'jobs': jobs, 'studies': studies, 'skills': skills}
    return render(request, 'cv/about.html', context)   


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST) #tried instance=blog and blog=blog
        if form.is_valid():
            form.save()
            #from printout... think there should be a cleaner way to do this
            messages.success(request, f'Thanks for your query, I will get back shortly!')
            #form = CommentForm() don't need with redirect
            return redirect('index')
    context = {'form': form} 

    return render(request, 'cv/contact.html', context)   
  
@login_required
def contacts(request):
    contacts = Contact.objects.all().order_by('reply', 'id') #order by oldest contacts without reply
    context = {'contacts': contacts}
    return render(request, 'cv/contacts.html', context)
