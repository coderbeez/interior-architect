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
from django.conf import settings
from django.conf.urls.static import static

# Credit: auth views Corey Schafer https://www.youtube.com/watch?v=3aVqWaLjqS4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=7
# settings & static 4 media https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=8

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('about/', include('cv.urls')),
    path('contact/', include('contact.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('cart/', include('cart.urls')),
    path('users/', include('users.urls')), # not how corey did it may need to change???
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), # class based views
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'), # handles forms & logic but not templates
]
# template name tells django where to look for the template

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# credit: Corey https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=8
# https://docs.djangoproject.com/en/3.0/howto/static-files/
# Used to serve image files uploaded by user during development