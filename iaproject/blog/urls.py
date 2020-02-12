from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('<pk>', views.blog, name='blog'),
    path('like/<pk>/', views.like, name='like'),
    path('comments/', views.comments, name='comments'),
    path('comments/<pk>/', views.comments, name='comments'),
]