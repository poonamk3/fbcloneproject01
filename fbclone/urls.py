"""fbclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
from api_view.api_views import registreviewapi
from rest_framework import routers
from rest_framework.authtoken import views
# from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

# Swagger
schema_view = get_swagger_view(title='Fbclone Project API')
# sentry
def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('login.urls')),
    path('api/',include('api_url.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('docs/', schema_view),   #Swagger link
    path('accounts/', include('allauth.urls')),
    # path('sentry-debug/', trigger_error),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# https://www.youtube.com/watch?v=9WFAuq_DD1E