import stripe
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from iaproject.settings import STRIPE_PUBLISHABLE, STRIPE_SECRET
from .models import Cart
from portfolio.models import Download

# Credit: Coding Point https://www.youtube.com/watch?v=5q3c3kYSRzk&list=PLPp4GCMxKSjCM9AvhmF9OHyyaJsN8rsZK&index=23

def cart(request):
    try:
        current_cart_id = request.session['cart_id']
        cart = Cart.objects.get(pk=current_cart_id)
    except: 
        current_cart_id = None 
        cart = None
        messages.error(request, f'A cart has not been created!')
    context = {'title': 'Cart', 'cart': cart}
    return render(request, 'cart/cart.html', context)

def add(request, pk): #make cart for first time when add
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
        new_total = 0.00
        for download in cart.downloads.all():
            new_total += float(download.price)
        cart.total = new_total
        cart.save()
        request.session['download_count'] = cart.downloads.count() 
        messages.success(request, f'{download.title} added to cart.')
    else: 
        messages.warning(request, f'{download.title} already in cart.')
    return redirect('project', pk=project) #request throws an error?
    #after u add to cart where do u want to go - assume u want to stay on project pg

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
        new_total = 0.00
        for download in cart.downloads.all():
            new_total += float(download.price)
        cart.total = new_total
        cart.save()
        request.session['download_count'] = cart.downloads.count() #create
        messages.success(request, f'{download.title} removed from cart.')
    #else:
        #messages.warning(request, f'Download is not in cart.')#do I need?
    return redirect('cart')       

def charge(request):
    current_cart_id = request.session['cart_id']
    cart = Cart.objects.get(pk=current_cart_id)
    items = []
    for download in cart.downloads.all():
        item = {'name': download.title, 'description': download.content, 'amount': int((download.price)*100), 'currency': 'eur', 'quantity': 1}
        items.append(item)
    stripe.api_key = STRIPE_SECRET
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=items,
        success_url=request.build_absolute_uri('/cart/success?session_id=')+'{CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri('/cart'),
        client_reference_id='A0'+str(cart.id)
        )
    context = {'sid': session.id,}
    return render(request, 'cart/charge.html', context)
    #Do i have to hard code success url?

def success(request):
    stripe.api_key = STRIPE_SECRET #got an error after heroku deploy needing this
    stripe_session = request.GET.get('session_id')
    stripe_data = stripe.checkout.Session.retrieve(stripe_session)
    cart_id = request.session['cart_id']
    cart = Cart.objects.get(pk=cart_id)
    cart.stripe = stripe_session
    cart.save() #saving the session id to cart model so have record and can see what carts were purchased
    del request.session['cart_id'] #can't purchase same cart twice
    context = {'title': 'Complete', 'stripe_data': stripe_data, }
    return render(request, 'cart/success.html', context)
    #https://stackoverflow.com/questions/150505/capturing-url-parameters-in-request-get
    #https://stackoverflow.com/questions/16039399/how-to-clear-all-session-variables-without-getting-logged-out