import stripe
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from iaproject.settings import STRIPE_PUBLISHABLE, STRIPE_SECRET
from .models import Cart
from portfolio.models import Download

# Credit: Coding Point https://www.youtube.com/watch?v=5q3c3kYSRzk&list=PLPp4GCMxKSjCM9AvhmF9OHyyaJsN8rsZK&index=23

def cart(request):
    '''Renders cart page.
    If it exists, gets current cart id from session.
    '''
    try:
        current_cart_id = request.session['cart_id']
        cart = Cart.objects.get(pk=current_cart_id)
    except: 
        current_cart_id = None 
        cart = None
        messages.error(request, f'A cart has not been created!')
    context = {'title': 'Cart', 'cart': cart}
    return render(request, 'cart/cart.html', context)

def add(request, pk):
    '''Adds a download to a cart.
    If it exists, gets current cart id from session.
    If it doesn't, creates a cart and adds its id to session.
    If passed download is not already in current cart, 
    updates download and total in cart, and
    cart count in session.
    ''' #Is passed the right term????
    try:
        current_cart_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        current_cart_id = request.session['cart_id']
    cart = Cart.objects.get(pk=current_cart_id)    
    download = get_object_or_404(Download, pk=pk)
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

def remove(request, pk):
    '''Removes a download from a cart.
    Gets current cart id from session.
    Removes passed download from cart.
    Updates cart total in cart, and cart count in session.
    '''
    cart = Cart.objects.get(pk=request.session['cart_id'])#Do I need 404 here?   
    download = get_object_or_404(Download, pk=pk)
    cart.downloads.remove(download)
    new_total = 0.00
    for download in cart.downloads.all():
        new_total += float(download.price)
    cart.total = new_total
    cart.save()
    request.session['download_count'] = cart.downloads.count()
    messages.success(request, f'{download.title} removed from cart.')
    return redirect('cart')       

def charge(request):
    '''Renders charge page and redirects payment to Stripe.
    Gets current cart id from session.
    Creates list of all downloads for current cart id.
    Creates Stripe checkout session as per Stripe documentation.
    Makes Stripe's session id availble in context.
    '''
    cart = Cart.objects.get(pk=request.session['cart_id'])#Do I need 404 here? 
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

def success(request):
    '''Renders success page.
    Gets Stripe's session id from url and uses to retrieve Stripe's session data.
    Gets current cart id from session.
    Saves Stripe's session id to cart as reference.
    Removes cart data from session to prevent repurchase errors.
    Makes Stripe's session data available in context.
    Credit: Capture url parameters https://stackoverflow.com/questions/150505/capturing-url-parameters-in-request-get
    Credit: Clear session https://stackoverflow.com/questions/16039399/how-to-clear-all-session-variables-without-getting-logged-out
    '''
    stripe.api_key = STRIPE_SECRET #got an error after heroku deploy needing this
    stripe_session = request.GET.get('session_id')
    stripe_data = stripe.checkout.Session.retrieve(stripe_session)
    cart = Cart.objects.get(pk=request.session['cart_id'])
    cart.stripe = stripe_session
    cart.save()
    del request.session['cart_id']
    del request.session['download_count']#1 line?
    context = {'title': 'Complete', 'stripe_data': stripe_data, }
    return render(request, 'cart/success.html', context)
    #????? Is the del in the right place here?????