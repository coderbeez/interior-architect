from django.contrib import admin
from .models import Cart


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'total', 'stripe', 'fulfilled')
    ordering = ('fulfilled', '-stripe', 'id',)
    list_display_links = ('id',)
    list_filter = ('fulfilled',)
    list_editable = ('fulfilled',)


admin.site.register(Cart, CartAdmin)
'''Credit: Display, filters, edits Brad Traversey
https://www.udemy.com/course/python-django-dev-to-deployment/
Credit: Order
https://stackoverflow.com/questions/4571916/django-admin-sort-order
'''
