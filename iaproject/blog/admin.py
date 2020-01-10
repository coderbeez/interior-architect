from django.contrib import admin
from .models import Blog, Comment

# Register your models here.
#admin.site.register(Post)
#admin.site.register(Comment)

class CommentInline(admin.TabularInline):
    model = Comment

class BlogAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    #from docs

admin.site.register(Blog, BlogAdmin)
