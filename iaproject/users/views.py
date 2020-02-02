from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm 


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

@login_required
def profile(request):# using 2 forms
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user) # POST the form data
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)# need the instance of current user
        # will also be getting image data ie FILES
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account updated!')
            return redirect('profile')
            # post get redirect pattern... redirect to profile sends a get request and prevents reload???
    else:
        u_form = UserUpdateForm(instance=request.user) # POST the form data
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = { 'u_form': u_form, 'p_form': p_form}
    return render(request, 'users/profile.html', context) #why can I access user. in template???   
# passing in instance so fields are prepopulated as its an update form