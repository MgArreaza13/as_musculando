"""Musculando URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
router =  routers.DefaultRouter()


from apps.Marketing.views import MailViewSet
router.register(r'api/Mails', MailViewSet)
#from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [
    url(r'^', include('apps.Panel.urls', namespace='Panel')),
    url(r'^admin/', admin.site.urls),
    url(r'^Clases/', include('apps.Clases.urls', namespace='Clases')),
    url(r'^Caja/', include('apps.Caja.urls', namespace='Caja')),
    url(r'^Configuracion/', include('apps.Configuracion.urls', namespace='Configuracion')),
    url(r'^Usuarios/', include('apps.UserProfile.urls', namespace='Usuarios')),
    url(r'^Proveedores/', include('apps.Proveedores.urls', namespace='Proveedores')),
    url(r'^Socios/', include('apps.Socios.urls', namespace='Socios')),
    url(r'^Marketing/', include('apps.Marketing.urls', namespace='Marketing')),
    
]
#urlpatterns += router.urls
urlpatterns += router.urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)