from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMultiAlternatives
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from .models import Contact
from .forms import ContactForm, ReplyForm

def contact(request):
    '''Render contact form.
    Create a contact on valid form save.
    Send email flag on valid from save.
    '''
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail('New Contact','You have a new contact.','cos.interior.architect@gmail.com',['sullivanedel@hotmail.com',],fail_silently=False,)
            messages.success(request, f'Thanks for your query, I will get back shortly!')
            return redirect('index')
        else:
            messages.error(request, f'Sorry something went wrong!')   
    context = {'title': 'Contact', 'form': form} 
    return render(request, 'contact/contact.html', context)

@login_required
def contacts(request, pk=None):
     ''' View accessed by site admin only, login required.
    Render outstanding contacts (i.e. not excluded and no reply), oldest first.
    Render reply form for each contact.
    Update individual contact on valid form post.
    If update is reply, send email, either text or html template.
    Credit: F strings https://realpython.com/python-f-strings/
    '''
    contacts = Contact.objects.filter(exclude=False, reply='').order_by('id')
    form = ReplyForm()
    if request.method == 'POST':
        contact = Contact.objects.get(pk=pk)
        form = ReplyForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            if contact.exclude:
                messages.success(request, f'{contact.name} contact closed.')
            elif contact.reply !='':   
                subject = 'Reply from COS Interior Architect'
                from_email = 'cos.interior.architect@gmail.com'
                to = [contact.email,]
                text_content = f"""
                Dear {contact.name}

                Many thanks you for your {contact.category} enquiry.

                QUERY: {contact.query} 

                REPLY: {contact.reply}

                Please do not hesitate to contact me with any further queries.

                All the best
                Colette O'Sullivan

                INTERIOR ARCHITECT & DESIGNER
                http://www.coletteosullivan.com/

                """
                html_template = get_template('contact/reply_email.html').render({'contact': contact, 'title': 'Contact Reply'})
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_template, "text/html")
                msg.send()               
                messages.success(request, f'{contact.name} emailed.')
            else:
                messages.warning(request, 'No change saved!')    
            return redirect('contacts')
        else:
            messages.error(request, f'Something went wrong!')      
    context = {'title': 'Contacts', 'contacts': contacts, 'form': form}
    return render(request, 'contact/contacts.html', context)