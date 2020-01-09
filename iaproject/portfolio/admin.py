from django.contrib import admin
from .models import Project, Section

# Register your models here.
#admin.site.register(Post)
#admin.site.register(Comment)

class SectionInline(admin.TabularInline):
    model = Section

class ProjectAdmin(admin.ModelAdmin):
    inlines = [SectionInline]
    #from docs

admin.site.register(Project, ProjectAdmin)
