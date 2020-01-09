from django.contrib import admin
from .models import Role, Point

# Register your models here.
#admin.site.register(Post)
#admin.site.register(Comment)

class PointInline(admin.TabularInline):
    model = Point

class RoleAdmin(admin.ModelAdmin):
    inlines = [PointInline]
    #from docs

admin.site.register(Role, RoleAdmin)

# Register your models here.
