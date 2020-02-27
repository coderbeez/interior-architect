from django import forms
from django.forms import Textarea
''' GetText Lazy imported to allow label to be blank
Credit: https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/
'''
from django.utils.translation import gettext_lazy as _
from .models import Contact


class ContactForm(forms.ModelForm):
    '''Create a contact.
    '''
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'location', 'category', 'query']


class ReplyForm(forms.ModelForm):
    '''
    Update a contact by adding data to the reply and/or exclude fields.
    Credit: Customising model form fields
    https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/
    Credit: Form widgets Coding Entrepreneurs
    https://www.youtube.com/watch?v=-oWIyFYyNQw
    '''
    class Meta:
        model = Contact
        fields = ['reply', 'exclude']
        labels = {'reply': _(''), 'exclude': _('exclude'), }
        widgets = {'reply': Textarea(
            attrs={'rows': 5, 'class': 'textarea-style'}
        ), }
