from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Role, Point, Example, Contact
from .forms import ContactForm

# Create your views here.

def about(request):
    roles = Role.objects.all().order_by('-id')
    context = {'roles': roles}
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
  
