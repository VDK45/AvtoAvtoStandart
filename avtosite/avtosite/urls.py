"""
URL configuration for avtosite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from avto_tochka.views import *
from django.urls import path, include

from avtosite import settings

urlpatterns = [
    path('admin/', admin.site.urls),  # http://127.0.0.1:8000/admin
    path('captcha/', include('captcha.urls')),
    path('', include('avto_tochka.urls')),

    # django-allauth
    path('accounts/', include('allauth.urls')),  # Django-allauth
]

if settings.DEBUG:  # import from avtosite
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound  # DEBUG = False
