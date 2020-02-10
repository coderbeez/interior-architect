from django.contrib import admin
from .models import Role, Point, Example, Skill

# Register your models here.

class PointInline(admin.TabularInline):
    model = Point

class ExampleInline(admin.TabularInline):
    model = Example

class RoleAdmin(admin.ModelAdmin):
    inlines = [PointInline, ExampleInline]
    #from docs

admin.site.register(Role, RoleAdmin)
admin.site.register(Skill)


