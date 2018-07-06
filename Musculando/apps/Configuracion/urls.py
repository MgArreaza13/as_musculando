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


#################TIPOS DE COLABORADORES#########################

from apps.Configuracion.views import DeleteTipoDeColaborador
from apps.Configuracion.views import NuevoTipoDeColaborador
from apps.Configuracion.views import GetTipoColaborador
from apps.Configuracion.views import UpdateTipoColaborador



##############################TIPO DE EGRESO###########################################
from apps.Configuracion.views import NuevoTipoDeEgreso
from apps.Configuracion.views import DeleteTipoDeEgreso
from apps.Configuracion.views import GetTipoEgreso
from apps.Configuracion.views import UpdateTipoEgreso


##############################TIPO DE INGRESO###########################################
from apps.Configuracion.views import NuevoTipoDeIngreso
from apps.Configuracion.views import DeleteTipoDeIngreso
from apps.Configuracion.views import GetTipoIngreso
from apps.Configuracion.views import UpdateTipoIngreso


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
  	#########################TIPO DE COLABORADORES#########################################
  	url(r'^Tipo/De/Colaboradores/Solicitud/Eliminar/Registro/$', DeleteTipoDeColaborador ,  name='DeleteTipoDeColaborador' ),
  	url(r'^Tipo/De/Colaboradores/Solicitud/Nuevo/Registro/$', NuevoTipoDeColaborador ,  name='NuevoTipoDeColaborador' ),
	url(r'^Tipo/De/Colaboradores/Get/Registro/$', GetTipoColaborador ,  name='GetTipoColaborador' ),
	url(r'^Tipo/De/Colaboradores/Update/Registro/$', UpdateTipoColaborador ,  name='UpdateTipoColaborador' ),
	##############################TIPO DE EGRESO###########################################
	url(r'^Tipo/De/Egreso/Solicitud/Eliminar/Registro/$', DeleteTipoDeEgreso ,  name='DeleteTipoDeEgreso' ),
  	url(r'^Tipo/De/Egreso/Solicitud/Nuevo/Registro/$', NuevoTipoDeEgreso ,  name='NuevoTipoDeEgreso' ),
	url(r'^Tipo/De/Egreso/Get/Registro/$', GetTipoEgreso ,  name='GetTipoEgreso' ),
	url(r'^Tipo/De/Egreso/Update/Registro/$', UpdateTipoEgreso ,  name='UpdateTipoEgreso' ),
	##############################TIPO DE INGRESO###########################################
	url(r'^Tipo/De/Ingreso/Solicitud/Eliminar/Registro/$', DeleteTipoDeIngreso ,  name='DeleteTipoDeIngreso' ),
  	url(r'^Tipo/De/Ingreso/Solicitud/Nuevo/Registro/$', NuevoTipoDeIngreso ,  name='NuevoTipoDeIngreso' ),
	url(r'^Tipo/De/Ingreso/Get/Registro/$', GetTipoIngreso ,  name='GetTipoIngreso' ),
	url(r'^Tipo/De/Ingreso/Update/Registro/$', UpdateTipoIngreso ,  name='UpdateTipoIngreso' ),



]