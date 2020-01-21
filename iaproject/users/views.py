from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Credit: Corey Schafer https://www.youtube.com/watch?v=q4jPR-M0TAQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=6
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) #intantiate a form with Post data
        if form.is_valid():
            username = form.cleaned_data.get('username') #python data
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form = UserCreationForm()
    #context = {'form': form}
    return render(request, 'users/register.html', {'form': form})
