from django.contrib import admin
from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'total', 'stripe', 'fulfilled')
    ordering = ('fulfilled', '-stripe','id',)
    list_display_links = ('id',)
    list_filter = ('fulfilled',)
    list_editable = ('fulfilled',)

admin.site.register(Cart, CartAdmin)
#credit brad real estate
