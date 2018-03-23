"""TesisDgiService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api/', include('apis.proceso_api.urls')),
    url(r'^api/proceso/', include('apis.proceso_api.urls')),
    url(r'^api/tesis-proceso/', include('apis.tesis_proceso_api.urls')),
    url(r'^api/proyecto/', include('apis.proyecto_api.urls')),
    url(r'^api/academico/', include('apis.academico_api.urls')),
    url(r'^api/config/', include('apis.config_api.urls')),
    # url(r'^api/', include('apis.tesis_proceso_api.urls')),
    # path('admin/doc/', include('django.contrib.admindocs.urls'))
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^refresh-token/', refresh_jwt_token),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
