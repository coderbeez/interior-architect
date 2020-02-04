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
    inlines = [SectionInline, DownloadInline]
    #from docs


admin.site.register(Category)
admin.site.register(Project, ProjectAdmin)
