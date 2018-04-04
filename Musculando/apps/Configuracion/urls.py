from django.conf.urls import url
from django.contrib import admin
#######################PLANES##############################
from apps.Configuracion.views import NuevoPlan
from apps.Configuracion.views import ListaDePlanes
from apps.Configuracion.views import EliminarPlan
from apps.Configuracion.views import getPlan
from apps.Configuracion.views import updatePlan
#####################CONFIGURACION############################
from apps.Configuracion.views import Configuracion_g
###################FORMASS DE PAGO############################
from apps.Configuracion.views import DeleteFormadePago
from apps.Configuracion.views import NewFormadePago
from apps.Configuracion.views import GetFormaDePago
from apps.Configuracion.views import UpdateFormaDePago
from apps.Configuracion.views import FormasdePagoGet

urlpatterns = [
	########################PLANES#########################################
	url(r'^Planes/Lista/$', ListaDePlanes ,  name='ListaDePlanes' ),
	url(r'^Planes/Solicitud/Nuevo/Registro/$', NuevoPlan ,  name='NuevoPlan' ),
	url(r'^Planes/Solicitud/Eliminar/Registro/$', EliminarPlan ,  name='EliminarPlan' ),
	url(r'^Planes/Solicitud/Get/Registro/$', getPlan ,  name='getPlan' ),
	url(r'^Planes/Solicitud/Update/Registro/$', updatePlan ,  name='updatePlan' ),
	#######################CONFIGURACION GENERAL ###################################
	url(r'^$', Configuracion_g, name='Configuracion_g' ),
	#########################FORMAS DE PAGO#########################################
	url(r'^Forma/De/Pago/Solicitud/Eliminar/Registro/$', DeleteFormadePago ,  name='DeleteFormadePago' ),
	url(r'^Forma/De/Pago/Solicitud/Nuevo/Registro/$', NewFormadePago ,  name='NewFormadePago' ),
	url(r'^Forma/De/Pago/Solicitud/Get/Registro/$', GetFormaDePago ,  name='GetFormaDePago' ),
	url(r'^Forma/De/Pago/Solicitud/Update/Registro/$', UpdateFormaDePago ,  name='UpdateFormaDePago' ),
  	url(r'^Forma/De/Pago/Solicitud/Get/$', FormasdePagoGet ,  name='FormasdePagoGet' ),
  
]