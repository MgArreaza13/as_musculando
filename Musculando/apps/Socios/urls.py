from django.conf.urls import url
from django.contrib import admin
from apps.Socios.views import ListaDeSocios
#from apps.Socios.views import DectivandoSocios
from apps.Socios.views import NewSocio
from apps.Socios.views import DeleteSocio
from apps.Socios.views import DesactivateSocio
from apps.Socios.views import ActivateSocio
from apps.Socios.views import getSocio
from apps.Socios.views import ActivacionSocioMensualAnual
from apps.Socios.views import UpdateSocio

#from apps.Proveedores.views import ListaDeProveedores
#from apps.Proveedores.views import Nuevo
#from apps.Proveedores.views import NuevoProveedor

urlpatterns = [
	#url(r'^registro/$', Registro, name='Registro'  ),
	#url(r'^editar/(?P<id_UserProfile>\d+)$', EditUserProfile, name='EditUserProfile'  ),
	#url(r'^borrar/(?P<id_UserProfile>\d+)$', DeleteUserProfile, name='DeleteUserProfile'  ),
	#url(r'^nuevousuario/$', NuevoUsuario, name='NuevoUsuario'  ),
	#url(r'^Nuevo/$', Nuevo, name='Nuevo'  ),
	#url(r'^Nueva/Peticion/de/Desactivacion/de/Socios$', DectivandoSocios, name='DectivandoSocios'  ),
	url(r'^Nueva/Peticion/de/Eliminacion/de/Socios$', DeleteSocio, name='DeleteSocio'  ),
	url(r'^Nueva/Peticion/de/Desactivar$', DesactivateSocio, name='DesactivateSocio'  ),
	url(r'^Nueva/Peticion/de/Obtener/Datos/Socios$', getSocio, name='getSocio'  ),

	url(r'^Nueva/Peticion/de/Activar$', ActivateSocio, name='ActivateSocio'  ),
	url(r'^Nueva/Peticion/de/Activar/Socio/$', ActivacionSocioMensualAnual, name='ActivacionSocioMensualAnual'  ),
	url(r'^Lista/$', ListaDeSocios , name='ListaDeSocios'  ),
	url(r'^Nuevo/$', NewSocio , name='NewSocio'  ),
	url(r'^Editar/(?P<id_socio>\d+)$', UpdateSocio, name='UpdateSocio'  ),
  
]