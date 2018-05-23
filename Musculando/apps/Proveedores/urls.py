from django.conf.urls import url
from django.contrib import admin
from apps.Proveedores.views import ListaDeProveedores
from apps.Proveedores.views import Nuevo
from apps.Proveedores.views import NuevoProveedor
from apps.Proveedores.views import DeleteProveedor
from apps.Proveedores.views import UpdateProveedor
from apps.Proveedores.views import NuevoUpdateAjax


urlpatterns = [
	#url(r'^registro/$', Registro, name='Registro'  ),

	url(r'^Editar/(?P<id_proveedor>\d+)$', UpdateProveedor, name='UpdateProveedor'  ),
	#url(r'^borrar/(?P<id_UserProfile>\d+)$', DeleteUserProfile, name='DeleteUserProfile'  ),
	#url(r'^nuevousuario/$', NuevoUsuario, name='NuevoUsuario'  ),
	url(r'^Nuevo/$', Nuevo, name='Nuevo'  ),
	url(r'^Nueva/Peticion/de/Nuevo/Proveedor$', NuevoProveedor, name='NuevoProveedor'  ),
	url(r'^Nueva/Peticion/de/Update/Proveedor$', NuevoUpdateAjax, name='NuevoUpdateAjax'  ),
	url(r'^Nueva/Peticion/de/Borrar/Proveedor$', DeleteProveedor, name='DeleteProveedor'  ),
	url(r'^Lista/$', ListaDeProveedores , name='ListaDeProveedores'  ),
  


]