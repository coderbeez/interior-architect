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