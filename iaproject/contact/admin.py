from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'date', 'exclude')
    ordering = ('exclude', 'reply', '-id')
    list_display_links = ('id', 'name')
    list_filter = ('exclude',)
    list_editable = ('exclude',)

admin.site.register(Contact, ContactAdmin)
# Credit: Display, filters, edits Brad Traversey https://www.udemy.com/course/python-django-dev-to-deployment/
# Credit: Order https://stackoverflow.com/questions/4571916/django-admin-sort-order