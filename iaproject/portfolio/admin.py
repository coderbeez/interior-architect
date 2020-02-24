from django.contrib import admin
from .models import Category, Project, Section, Download

# Register your models here.
#admin.site.register(Post)
#admin.site.register(Comment)

class SectionInline(admin.TabularInline):
    model = Section

class DownloadInline(admin.TabularInline):
    model = Download

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'category', 'home', 'exclude')
    ordering = ('exclude', 'order')
    list_display_links = ('title',)
    list_filter = ('home', 'exclude')
    list_editable = ('order', 'home', 'exclude')
    inlines = [SectionInline, DownloadInline]

admin.site.register(Category)
admin.site.register(Project, ProjectAdmin)
# Credit: Inlines https://stackoverflow.com/questions/14308050/django-admin-nested-inline
# Credit: Display, filters, edits Brad Traversey https://www.udemy.com/course/python-django-dev-to-deployment/
# Credit: Order https://stackoverflow.com/questions/4571916/django-admin-sort-order
