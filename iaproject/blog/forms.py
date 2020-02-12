from django import forms
from django.forms import Textarea #this is what django docs import
from django.utils.translation import gettext_lazy as _ #imported to allow label to be blank - from django docs (link below)
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content': _(''),}
        widgets = {'content': Textarea(attrs={'rows':5, 'class': 'textarea-style'}),}
    #customising model form fields from django docs https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/
    #Credit: Coding Entrepreneurs Try DJANGO Tutorial - 26 - Form Widgets https://www.youtube.com/watch?v=-oWIyFYyNQw

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['reply', 'exclude']
        labels = {'reply': _(''), 'exclude': _('exclude'),}
        widgets = {'reply': Textarea(attrs={'rows':5, 'class': 'textarea-style'}),}