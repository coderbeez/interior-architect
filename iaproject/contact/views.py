from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Contact
from .forms import ContactForm, ReplyForm

# Create your views here.

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST) #tried instance=blog and blog=blog
        if form.is_valid():
            form.save()
            send_mail('New Contact','You have a new contact.','cos.interior.architect@gmail.com',['coletteo32@gmail.com', 'sullivanedel@hotmail.com'],fail_silently=False,)
            #django docs
            messages.success(request, f'Thanks for your query, I will get back shortly!')
            return redirect('index')
    context = {'title': 'Contact', 'form': form} 

    return render(request, 'contact/contact.html', context)   
  

@login_required
def contacts(request, pk=None):
    contacts = Contact.objects.filter(exclude=False, reply='').order_by('id') #order by oldest without reply
    form = ReplyForm()

    if pk:
        contact = Contact.objects.get(pk=pk)

    #Credit: https://stackoverflow.com/questions/38046905/sending-post-data-from-inside-a-django-template-for-loop

        if request.method == 'POST':
            form = ReplyForm(request.POST, instance=contact) # POST the form data
            if form.is_valid():
                form.save()
                if contact.exclude:
                    messages.success(request, f'{contact.name} contact closed.')
                elif contact.reply !='':
                    send_mail('Reply from COS Interior Architect',
                    f"""
                    Dear {contact.name}

                    Many thanks you for your {contact.category} enquiry.

                    QUERY: {contact.query} 

                    REPLY: {contact.reply}

                    Please do not hesitate to contact me with any further queries.

                    All the best
                    Colette O'Sullivan

                    INTERIOR ARCHITECT & DESIGNER
                    http://www.coletteosullivan.com/

                    """,
                    'cos.interior.architect@gmail.com',
                    [contact.email,],
                    fail_silently=False,)
                    messages.success(request, f'{contact.name} emailed.')
                else:
                    messages.success(request, 'No change saved.')    
                return redirect('contacts')

    context = {'title': 'Contacts', 'contacts': contacts, 'form': form}
    return render(request, 'contact/contacts.html', context)    

#https://realpython.com/python-f-strings/