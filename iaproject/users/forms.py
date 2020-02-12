from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm): # form inherits from UserCreationForm
    email = forms.EmailField() # and adds the email field

    class Meta: #specify the model want the form to interact with
        #nested namespace for configurations???
        #keeps configurations in one space
        #says model that will be affected will be the user model
        model = User #when form validates its going to create a new user
        fields = ['username', 'email', 'password1', 'password2'] #fields we want to be shown and the order
# Credit: Corey Scahfer https://www.youtube.com/watch?v=q4jPR-M0TAQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=6

# a model form is a form that will work with a specific model
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
# Credit Corey https://www.youtube.com/watch?v=CQ90L5jfldw&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=9    