from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    # path('<pk>', views.project, name='project'),
]