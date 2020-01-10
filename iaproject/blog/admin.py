from django.contrib import admin
from .models import Blog, Section, Comment

# Register your models here.
#admin.site.register(Post)
#admin.site.register(Comment)

class SectionInline(admin.TabularInline):
    model = Section

class CommentInline(admin.TabularInline):
    model = Comment

class BlogAdmin(admin.ModelAdmin):
    inlines = [SectionInline, CommentInline]
    #from docs

admin.site.register(Blog, BlogAdmin)
