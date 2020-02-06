from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    #path('<pk>', views.blog, name='blog'),

]