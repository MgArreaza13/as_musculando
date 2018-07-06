from django.conf.urls import url
from django.contrib import admin
from apps.Colaboradores.views import ListaDeColaboradores
from apps.Colaboradores.views import EliminarColaborador
from apps.Colaboradores.views import NewColaborador
from apps.Colaboradores.views import UpdateColaboradores
from apps.Colaboradores.views import CuentaColaborador
from apps.Colaboradores.views import Liquidacion
from apps.Colaboradores.views import ProcesoDeLiquidacion
from apps.Colaboradores.views import Presentimo
from apps.Colaboradores.views import ProcesoDePresentimo
#from apps.Panel.views import Inicio
#from apps.Panel.views import Login
#from apps.Panel.views import ComingSoon
#from apps.Panel.views import Logout


urlpatterns = [
	url(r'^Lista/$', ListaDeColaboradores , name='ListaDeColaboradores'  ),
	url(r'^Liquidacion/$', Liquidacion , name='Liquidacion'  ),
	url(r'^Presentimo/$', Presentimo , name='Presentimo'  ),
	url(r'^Solicitud/Para/eliminar/Colaborador$', EliminarColaborador , name='EliminarColaborador'  ),
	url(r'^Solicitud/Para/Procesar/Liquidacion/de/Colaboradores$', ProcesoDeLiquidacion , name='ProcesoDeLiquidacion'  ),
	url(r'^Solicitud/Para/Procesar/Presentimo/de/Colaboradores$', ProcesoDePresentimo , name='ProcesoDePresentimo'  ),
	url(r'^Nuevo/$', NewColaborador , name='NewColaborador'  ),
	url(r'^Editar/(?P<id_colaborador>\d+)$', UpdateColaboradores , name='UpdateColaboradores'  ),
	url(r'^Cuenta/(?P<id_colaborador>\d+)$', CuentaColaborador , name='CuentaColaborador'  ),

	#url(r'^$', Inicio, name='Inicio' ),
	#url(r'^Entrar/$', Login, name='Login' ),
	#url(r'^Viene/Pronto$', ComingSoon, name='ComingSoon' ),
	#url(r'^Salir/$', Logout, name='Logout' ),
	#url(r'^calendario/$', calendario, name='calendario' ),
	#url(r'^ingresosegresos/$', ingresosegresos, name='ingresoegresos' ),
	#url(r'^bloqueado/$', loockscreen ,  name='bloqueado' ),
	#url(r'^registro/$', registro ),
  
]