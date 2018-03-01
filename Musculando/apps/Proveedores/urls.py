from django.conf.urls import url
from django.contrib import admin
from apps.Proveedores.views import ListaDeProveedores
from apps.Proveedores.views import Nuevo
from apps.Proveedores.views import NuevoProveedor

urlpatterns = [
	#url(r'^registro/$', Registro, name='Registro'  ),
	#url(r'^editar/(?P<id_UserProfile>\d+)$', EditUserProfile, name='EditUserProfile'  ),
	#url(r'^borrar/(?P<id_UserProfile>\d+)$', DeleteUserProfile, name='DeleteUserProfile'  ),
	#url(r'^nuevousuario/$', NuevoUsuario, name='NuevoUsuario'  ),
	url(r'^Nuevo/$', Nuevo, name='Nuevo'  ),
	url(r'^Nueva/Peticion/de/Nuevo/Proveedor$', NuevoProveedor, name='NuevoProveedor'  ),
	url(r'^Lista/$', ListaDeProveedores , name='ListaDeProveedores'  ),
  
]