from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/<pk>/', views.contacts, name='contacts'),
]
