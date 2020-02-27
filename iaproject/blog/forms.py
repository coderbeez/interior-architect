from django import forms
from django.forms import Textarea
''' Get Text Lazy imported to allow label to be blank
Credit: https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/
'''
from django.utils.translation import gettext_lazy as _
from .models import Comment


class CommentForm(forms.ModelForm):
    '''
    Create a comment by adding data to the content field.
    Credit: Customising model form fields
    https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/
    Credit: Form widgets Coding Entrepreneurs
    https://www.youtube.com/watch?v=-oWIyFYyNQw
    '''
    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content': _(''), }
        widgets = {'content': Textarea(
            attrs={'rows': 5, 'class': 'textarea-style'}
        ), }


class ReplyForm(forms.ModelForm):
    '''
    Update a comment by adding data to the reply and/or exclude fields.
    '''
    class Meta:
        model = Comment
        fields = ['reply', 'exclude']
        labels = {'reply': _(''), 'exclude': _('exclude')}
        widgets = {'reply': Textarea(
            attrs={'rows': 5, 'class': 'textarea-style'}
        ), }
