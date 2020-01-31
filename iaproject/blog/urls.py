from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('<pk>', views.blog, name='blog'),
    path('comments/', views.comments, name='comments'),
]