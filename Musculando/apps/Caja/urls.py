from django.conf.urls import url
from django.contrib import admin
from apps.Caja.views import NewMensualIngreso
from apps.Caja.views import NuevoReporteDePagoMensual
from apps.Caja.views import ListadoDeIngresos
from apps.Caja.views import ListEgresos
from apps.Caja.views import Resumen
from apps.Caja.views import NewEgreso
from apps.Caja.views import ListOtroIngresos
from apps.Caja.views import NewIngreso
from apps.Caja.views import QueryAnual
from apps.Caja.views import QueryMensual
from apps.Caja.views import QueryDia
from apps.Caja.views import QueryTipoEgreso
from apps.Caja.views import Cierre
from apps.Caja.views import VerCierre
from apps.Caja.views import ResumenCierres

urlpatterns = [
	#url(r'^registro/$', Registro, name='Registro'  ),
	#url(r'^editar/(?P<id_UserProfile>\d+)$', EditUserProfile, name='EditUserProfile'  ),
	#url(r'^borrar/(?P<id_UserProfile>\d+)$', DeleteUserProfile, name='DeleteUserProfile'  ),
	#url(r'^nuevousuario/$', NuevoUsuario, name='NuevoUsuario'  ),
	url(r'^Resumen/$', Resumen, name='Resumen'  ),
	url(r'^Cierre/$', Cierre, name='Cierre'  ),
	url(r'^Cierre/Resumen$', ResumenCierres, name='ResumenCierres'  ),
	url(r'^Cierre/ver/(?P<id_cierre>\d+)$', VerCierre, name='VerCierre'  ),
	#url(r'^Nueva/Peticion/de/Nuevo/Proveedor$', NuevoProveedor, name='NuevoProveedor'  ),
	url(r'^Ingresos/Lista$', ListOtroIngresos , name='ListOtroIngresos'  ),
	url(r'^Ingresos/Mensualidad/Lista$', ListadoDeIngresos , name='ListadoDeIngresos'  ),
	url(r'^Egresos/Lista/$', ListEgresos , name='ListEgresos'  ),
	url(r'^Egresos/Nuevo/$', NewEgreso , name='NewEgreso'  ),
	url(r'^Ingresos/Nuevo/$', NewIngreso , name='NewIngreso'  ),
	url(r'^Ingresos/QueryAnual/$', QueryAnual , name='QueryAnual'  ),
	url(r'^Ingresos/QueryMensual/$', QueryMensual , name='QueryMensual'  ),
	url(r'^Ingresos/QueryDia/$', QueryDia , name='QueryDia'  ),
	url(r'^Ingresos/QueryTipoEgreso/$', QueryTipoEgreso , name='QueryTipoEgreso'  ),
	url(r'^Nuevo/Pago/De/Mensualidad/$', NewMensualIngreso , name='NewMensualIngreso'  ),
  	url(r'^Nueva/Solicitud/Pago/De/Mensualidad/$', NuevoReporteDePagoMensual , name='NuevoReporteDePagoMensual'  ),
]