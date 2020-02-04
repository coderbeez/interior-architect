from django.contrib import admin
from .models import Category, Blog, Section

# Register your models here.

class SectionInline(admin.TabularInline):
    model = Section

class BlogAdmin(admin.ModelAdmin):
    inlines = [SectionInline]
    #from docs

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)


#https://github.com/s-block/django-nested-inline
#https://stackoverflow.com/questions/14308050/django-admin-nested-inline