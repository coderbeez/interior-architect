from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import Category, Blog, Section, Bullet, Comment

# Register your models here.

class BulletInline(NestedStackedInline):
    model = Bullet

class SectionInline(NestedStackedInline):
    model = Section
    inlines = [BulletInline]

class CommentInline(NestedStackedInline):
    model = Comment

class BlogAdmin(NestedModelAdmin):
    model = Blog
    inlines = [SectionInline, CommentInline]
    #from docs

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)


#https://github.com/s-block/django-nested-inline