from django.urls import path
from .views import ProjectListView, ProjectDetailView #class based views
from . import views

urlpatterns = [
    #path('', views.projects, name='projects'),
    path('', ProjectListView.as_view(), name='projects'),
    #path('<pk>', views.project, name='project'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project'),
]