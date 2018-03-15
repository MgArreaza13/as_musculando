from django.conf.urls import url
from django.contrib import admin
from apps.Caja.views import NewMensualIngreso
from apps.Caja.views import NuevoReporteDePagoMensual
from apps.Caja.views import ListadoDeIngresos

urlpatterns = [
	#url(r'^registro/$', Registro, name='Registro'  ),
	#url(r'^editar/(?P<id_UserProfile>\d+)$', EditUserProfile, name='EditUserProfile'  ),
	#url(r'^borrar/(?P<id_UserProfile>\d+)$', DeleteUserProfile, name='DeleteUserProfile'  ),
	#url(r'^nuevousuario/$', NuevoUsuario, name='NuevoUsuario'  ),
	#url(r'^Nuevo/$', Nuevo, name='Nuevo'  ),
	#url(r'^Nueva/Peticion/de/Nuevo/Proveedor$', NuevoProveedor, name='NuevoProveedor'  ),
	url(r'^Ingresos/Lista/$', ListadoDeIngresos , name='ListadoDeIngresos'  ),
	url(r'^Nuevo/Pago/De/Mensualidad/$', NewMensualIngreso , name='NewMensualIngreso'  ),
  	url(r'^Nueva/Solicitud/Pago/De/Mensualidad/$', NuevoReporteDePagoMensual , name='NuevoReporteDePagoMensual'  ),
]