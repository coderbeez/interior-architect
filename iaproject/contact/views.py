from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import get_template
from .models import Contact
from .forms import ContactForm, ReplyForm

def contact(request):
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
    #send mail from django docs 

@login_required
def contacts(request, pk=None):
    contacts = Contact.objects.filter(exclude=False, reply='').order_by('id') #order by oldest without reply
    form = ReplyForm()

    if request.method == 'POST':
        contact = Contact.objects.get(pk=pk)
        form = ReplyForm(request.POST, instance=contact) # POST the form data
        if form.is_valid():
            form.save()
            if contact.exclude:
                messages.success(request, f'{contact.name} contact closed.')
            elif contact.reply !='':
                



                #subject, from_email, to = 'hello', 'from@example.com', 'to@example.com'    
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
                #html_content = "<h1>hello</h1><a href='https://www.coletteosullivan.com'>click</a>"
                html_template = get_template('contact/reply_email.html').render()
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_template, "text/html")
                msg.send()               
                #send_mail(subject, message, html_message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None,
                #connection=None, html_message=html_message)
                messages.success(request, f'{contact.name} emailed.')
            else:
                messages.warning(request, 'No change saved!')    
            return redirect('contacts')
        else:
            messages.error(request, f'Something went wrong!')      
    context = {'title': 'Contacts', 'contacts': contacts, 'form': form}
    return render(request, 'contact/contacts.html', context)    
    #https://realpython.com/python-f-strings/
    #Credit: https://stackoverflow.com/questions/38046905/sending-post-data-from-inside-a-django-template-for-loop

'''send_mail('Reply from COS Interior Architect',
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
                '''