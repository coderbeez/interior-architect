"""iaproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

# Credit: auth views Corey Schafer https://www.youtube.com/watch?v=3aVqWaLjqS4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=7

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('cv/', include('cv.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('users/', include('users.urls')), # not how corey did it may need to change???
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), # class based views
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'), # handles forms & logic but not templates
]
# template name tells django where to look for the template