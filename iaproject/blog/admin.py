from django.contrib import admin
from .models import Post, Comment

# Register your models here.
#admin.site.register(Post)
#admin.site.register(Comment)

class CommentInline(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    #from docs

admin.site.register(Post, PostAdmin)
