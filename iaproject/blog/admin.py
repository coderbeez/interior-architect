from django.contrib import admin
from .models import Category, Blog, Section, Bullet, Comment

# Register your models here.

class BulletInline(admin.StackedInline):
    model = Bullet

class SectionInline(admin.StackedInline):
    model = Section

class CommentInline(admin.StackedInline):
    model = Comment

class BlogAdmin(admin.ModelAdmin):
    inlines = [SectionInline, CommentInline]
    #from docs

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)


