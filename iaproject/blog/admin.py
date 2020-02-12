from django.contrib import admin
from .models import Category, Blog, Section

class SectionInline(admin.TabularInline):
    model = Section

class BlogAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'category', 'like', 'exclude')
    ordering = ('exclude','order')
    list_display_links = ('title',)
    list_filter = ('exclude',)
    list_editable = ('order', 'exclude')
    inlines = [SectionInline]

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)

#https://github.com/s-block/django-nested-inline
#https://stackoverflow.com/questions/14308050/django-admin-nested-inline
#from docs & Brad Traversey
#https://stackoverflow.com/questions/4571916/django-admin-sort-order