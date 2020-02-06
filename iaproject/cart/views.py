from django.shortcuts import render
from .models import Cart

# Create your views here.

def cart(request):
    cart = Cart.objects.all()[0]
    context = {'title': 'Cart', 'cart': cart}
    return render(request, 'cart/cart.html', context)
