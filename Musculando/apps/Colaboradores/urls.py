from django.conf.urls import url
from django.contrib import admin
from apps.Colaboradores.views import ListaDeColaboradores
from apps.Colaboradores.views import EliminarColaborador
from apps.Colaboradores.views import NewColaborador
from apps.Colaboradores.views import UpdateColaboradores
from apps.Colaboradores.views import CuentaColaborador
from apps.Colaboradores.views import getColaborador
from apps.Colaboradores.views import ProcesoDeLiquidacion
from apps.Colaboradores.views import ProcesarLiquidacion
from apps.Colaboradores.views import EntradaSalida
from apps.Colaboradores.views import ListEntradaSalida



urlpatterns = [
	url(r'^Lista/$', ListaDeColaboradores , name='ListaDeColaboradores'  ),
	url(r'^ControlDeAcceso/$', ListEntradaSalida , name='ListEntradaSalida'  ),
	url(r'^Solicitud/Para/eliminar/Colaborador$', EliminarColaborador , name='EliminarColaborador'  ),
	url(r'^Solicitud/Para/EntradoSalida/Colaborador$', EntradaSalida , name='EntradaSalida'  ),
	url(r'^Solicitud/Get/Colaborador$', getColaborador , name='getColaborador'  ),
	url(r'^Solicitud/Para/Procesar/Liquidacion/de/Colaboradores$', ProcesarLiquidacion , name='ProcesarLiquidacion'  ),
	url(r'^Nuevo/$', NewColaborador , name='NewColaborador'  ),
	url(r'^Editar/(?P<id_colaborador>\d+)$', UpdateColaboradores , name='UpdateColaboradores'  ),
	url(r'^Cuenta/(?P<id_colaborador>\d+)$', CuentaColaborador , name='CuentaColaborador'  ),
  
]