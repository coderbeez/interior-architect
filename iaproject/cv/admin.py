from django.contrib import admin
from .models import Role, Point, Example, Skill

class PointInline(admin.TabularInline):
    model = Point

class ExampleInline(admin.TabularInline):
    model = Example

class RoleAdmin(admin.ModelAdmin):
    list_display = ('order', 'job', 'title', 'company', 'timeframe')
    ordering = ('-job', '-order',)
    list_display_links = ('title',)
    list_filter = ('job',)
    list_editable = ('order',)
    inlines = [PointInline, ExampleInline]

admin.site.register(Role, RoleAdmin)
admin.site.register(Skill)
# Credit: Inlines https://stackoverflow.com/questions/14308050/django-admin-nested-inline
# Credit: Display, filters, edits Brad Traversey https://www.udemy.com/course/python-django-dev-to-deployment/
# Credit: Order https://stackoverflow.com/questions/4571916/django-admin-sort-order