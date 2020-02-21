from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Credit: Corey Schafer https://www.youtube.com/watch?v=q4jPR-M0TAQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=6
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #intantiate a form with Post data
        if form.is_valid():
            form.save() #hashes password etc
            username = form.cleaned_data.get('username') #python data
            messages.success(request, f'Account created for {username}! You can now login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {'title': 'Register', 'form': form}
    return render(request, 'users/register.html', context)