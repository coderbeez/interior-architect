from django import forms
from django.contrib.auth.models import User #not sure why importing model?
from django.contrib.auth.forms import UserCreationForm 

# Credit: Corey Scahfer https://www.youtube.com/watch?v=q4jPR-M0TAQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=6

class UserRegisterForm(UserCreationForm): # form inherits from UserCreationForm
    email = forms.EmailField() # and adds the email field

    class Meta: #specify the model want the form to interact with
        #nested namespace for configurations???
        #keeps configurations in one space
        #says model that will be affected will be the user model
        model = User #when form validates its going to create a new user
        fields = ['username', 'email', 'password1', 'password2'] #fields we want to be shown and the order
