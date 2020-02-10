from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Contact
from .forms import ContactForm, ReplyForm

# Create your views here.

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
    context = {'title': 'Contact', 'form': form} 

    return render(request, 'contact/contact.html', context)   
  

@login_required
def contacts(request, pk=None):
    contacts = Contact.objects.filter(reply='').order_by('id') #order by oldest without reply
    form = ReplyForm()

    if pk:
        contact = Contact.objects.get(pk=pk)

    #Credit: https://stackoverflow.com/questions/38046905/sending-post-data-from-inside-a-django-template-for-loop

    if request.method == 'POST':
        form = ReplyForm(request.POST, instance=contact) # POST the form data
        if form.is_valid():
            form.save()
            messages.success(request, f'Contact reply saved')
            return redirect('contacts')

    context = {'title': 'Contacts', 'contacts': contacts, 'form': form}
    return render(request, 'contact/contacts.html', context)    
