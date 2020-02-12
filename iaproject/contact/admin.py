from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'date', 'exclude')
    ordering = ('exclude', 'reply', '-id')
    list_display_links = ('id', 'name')
    list_filter = ('exclude',)
    list_editable = ('exclude',)

admin.site.register(Contact, ContactAdmin)
#credit brad real estate