from django.shortcuts import render, redirect
from django.contrib import messages
from portfolio.models import Download
from .models import Cart

# Create your views here.
# Credit: Coding Point https://www.youtube.com/watch?v=5q3c3kYSRzk&list=PLPp4GCMxKSjCM9AvhmF9OHyyaJsN8rsZK&index=23

def cart(request):
    try:
        current_cart_id = request.session['cart_id']
        cart = Cart.objects.get(pk=current_cart_id)
    except: 
        current_cart_id = None 
        cart = None
        messages.success(request, f'A cart has not been created.')
    context = {'title': 'Cart', 'cart': cart}
    return render(request, 'cart/cart.html', context)

def add(request, pk): #make cart for first time when add
    #cart = Cart.objects.all()[0]
    try: #checking to see if theres a cart id in session already
        current_cart_id = request.session['cart_id'] #request has a session attribute with key value pairs
    except: #if not create it
        new_cart = Cart()# new instance of model
        new_cart.save()
        request.session['cart_id'] = new_cart.id #create
        current_cart_id = request.session['cart_id']

    cart = Cart.objects.get(pk=current_cart_id)    
    download = Download.objects.get(pk=pk)
    project = download.project.id
    if not download in cart.downloads.all():
        cart.downloads.add(download)
        new_count = 0
        new_total = 0.00
        for download in cart.downloads.all():
            new_count += 1
            new_total += float(download.price)
        cart.count = new_count
        cart.total = new_total
        cart.save()
        messages.success(request, f'{download.title} added to cart.')
        #cart.total += download.price
        #cart.save()
    else: 
        messages.success(request, f'{download.title} already in cart.')
    return redirect('project', pk=project)   #don't need reverse... i think built in... request throws an error
# after u add to cart where do u want to go?


def remove(request, pk):
    try: #checking to see if theres a cart id in session already
        current_cart_id = request.session['cart_id'] #request has a session attribute with key value pairs
    except: #if not create it
        new_cart = Cart()# new instance of model
        new_cart.save()
        request.session['cart_id'] = new_cart.id #create
        current_cart_id = request.session['cart_id']

    cart = Cart.objects.get(pk=current_cart_id)    
    download = Download.objects.get(pk=pk)
    if download in cart.downloads.all():
        cart.downloads.remove(download)
        new_count = 0
        new_total = 0.00
        for download in cart.downloads.all():
            new_count += 1
            new_total += float(download.price)
        cart.count = new_count
        cart.total = new_total
        cart.save()
        messages.success(request, f'{download.title} removed from cart.')
    #else:
        #messages.success(request, f'Download not in cart.')  
    return redirect('cart')   #do i need reverse????          



