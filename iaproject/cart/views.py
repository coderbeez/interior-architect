from django.shortcuts import render, redirect
from django.contrib import messages
from portfolio.models import Download
from .models import Cart

# Create your views here.
# Credit: Coding Point https://www.youtube.com/watch?v=5q3c3kYSRzk&list=PLPp4GCMxKSjCM9AvhmF9OHyyaJsN8rsZK&index=23

def cart(request):
    cart = Cart.objects.all()[0]
    context = {'title': 'Cart', 'cart': cart}
    return render(request, 'cart/cart.html', context)

def add(request, pk):
    cart = Cart.objects.all()[0]
    download = Download.objects.get(pk=pk)
    project = download.project.id
    if not download in cart.downloads.all():
        cart.downloads.add(download)
        messages.success(request, f'Download added to cart.')
    else: 
        messages.success(request, f'Download already in cart.')
    return redirect('project', pk=project)   #don't need reverse... i think built in... request throws an error
# after u add to cart where do u want to go?


def remove(request, pk):
    cart = Cart.objects.all()[0]
    download = Download.objects.get(pk=pk)
    if download in cart.downloads.all():
        cart.downloads.remove(download)
        messages.success(request, f'Download removed from cart.')
    #else:
        #messages.success(request, f'Download not in cart.')  
    return redirect('cart')   #do i need reverse????          



