from django.contrib import admin
from .models import Category, Blog, Section, Comment


class SectionInline(admin.TabularInline):
    model = Section


class BlogAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'category', 'like', 'exclude')
    ordering = ('exclude', 'order')
    list_display_links = ('title',)
    list_filter = ('exclude',)
    list_editable = ('order', 'exclude')
    inlines = [SectionInline]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'blog','exclude')
    ordering = ('exclude', '-id')
    list_display_links = ('id',)
    list_filter = ('exclude',)


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(CommentAdmin)
'''Credit: Inlines
https://stackoverflow.com/questions/14308050/django-admin-nested-inline
Credit: Display, filters, edits Brad Traversey
https://www.udemy.com/course/python-django-dev-to-deployment/
Credit: Order
https://stackoverflow.com/questions/4571916/django-admin-sort-order
'''
