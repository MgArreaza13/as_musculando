from django.conf.urls import url
from django.contrib import admin
#######################PLANES##############################
from apps.Configuracion.views import NuevoPlan
from apps.Configuracion.views import ListaDePlanes
from apps.Configuracion.views import EliminarPlan
from apps.Configuracion.views import getPlan
from apps.Configuracion.views import updatePlan
from apps.Configuracion.views import NuevoPlanDiario
from apps.Configuracion.views import ListaDePlanes_diarios
from apps.Configuracion.views import EliminarPlanDiario
from apps.Configuracion.views import getPlanDiario
from apps.Configuracion.views import updatePlanDiario
#####################CONFIGURACION############################
from apps.Configuracion.views import Configuracion_g
###################FORMASS DE PAGO############################
from apps.Configuracion.views import DeleteFormadePago
from apps.Configuracion.views import NewFormadePago
from apps.Configuracion.views import GetFormaDePago
from apps.Configuracion.views import UpdateFormaDePago
from apps.Configuracion.views import FormasdePagoGet
#################TIPOS DE COLABORADORES######################
from apps.Configuracion.views import DeleteTipoDeColaborador
from apps.Configuracion.views import NuevoTipoDeColaborador
from apps.Configuracion.views import GetTipoColaborador
from apps.Configuracion.views import UpdateTipoColaborador
##############################TIPO DE EGRESO###############
from apps.Configuracion.views import NuevoTipoDeEgreso
from apps.Configuracion.views import DeleteTipoDeEgreso
from apps.Configuracion.views import GetTipoEgreso
from apps.Configuracion.views import UpdateTipoEgreso
##############################TIPO DE INGRESO############
from apps.Configuracion.views import NuevoTipoDeIngreso
from apps.Configuracion.views import DeleteTipoDeIngreso
from apps.Configuracion.views import GetTipoIngreso
from apps.Configuracion.views import UpdateTipoIngreso
##########################Horario########################
from apps.Configuracion.views import NuevoTipoTurno
from apps.Configuracion.views import DeleteTipoDeTurno
from apps.Configuracion.views import UpdateTipoTurno
from apps.Configuracion.views import GetTipoTurno
##########################PORCENTAJES####################
from apps.Configuracion.views import NewPorcentaje
from apps.Configuracion.views import UpdatePorcentaje
from apps.Configuracion.views import GetPorcentaje
from apps.Configuracion.views import DeletePorcentaje
from apps.Configuracion.views import PorcentajesoptionsGet
from apps.Configuracion.views import getDescuento
######################MAILS####################
from apps.Configuracion.views import NewMail
from apps.Configuracion.views import DeleteMail
from apps.Configuracion.views import GetMail
from apps.Configuracion.views import UpdateMail
####################TERMINOS###################
from apps.Configuracion.views import NewTermino
from apps.Configuracion.views import DeleteTermino
from apps.Configuracion.views import GetTermino
from apps.Configuracion.views import UpdateTermino
from apps.Configuracion.views import getTerminoView
from apps.Configuracion.views import enviartermino
from apps.Configuracion.views import recibodeid



urlpatterns = [
	########################PLANES#########################################
	url(r'^Planes/Lista/$', ListaDePlanes ,  name='ListaDePlanes' ),
	url(r'^Planes/Solicitud/Nuevo/Registro/$', NuevoPlan ,  name='NuevoPlan' ),
	url(r'^Planes/Solicitud/Eliminar/Registro/$', EliminarPlan ,  name='EliminarPlan' ),
	url(r'^Planes/Solicitud/Get/Registro/$', getPlan ,  name='getPlan' ),
	url(r'^Planes/Solicitud/Update/Registro/$', updatePlan ,  name='updatePlan' ),
	#############################PLANES DIARIOS###############################
	url(r'^Planes/Diarios/Lista/$', ListaDePlanes_diarios ,  name='ListaDePlanes_diarios' ),
	url(r'^Planes/Diarios/Solicitud/Nuevo/Registro/$', NuevoPlanDiario ,  name='NuevoPlanDiario' ),
	url(r'^Planes/Diarios/Solicitud/Eliminar/Registro/$', EliminarPlanDiario ,  name='EliminarPlanDiario' ),
	url(r'^Planes/Diarios/Solicitud/Get/Registro/$', getPlanDiario ,  name='getPlanDiario' ),
	url(r'^Planes/Diarios/Solicitud/Update/Registro/$', updatePlanDiario ,  name='updatePlanDiario' ),
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
	##########################Horario####################################
	url(r'^TipoTurno/Nuevo/$', NuevoTipoTurno , name='NuevoTipoTurno'  ),
	url(r'^Tipo/De/Turno/Solicitud/Eliminar/Registro/$', DeleteTipoDeTurno ,  name='DeleteTipoDeTurno' ),
	url(r'^Tipo/De/Turno/Get/Registro/$', GetTipoTurno ,  name='GetTipoTurno' ),
	url(r'^Tipo/De/Turno/Update/Registro/(?P<id_tipo_de_turno>\d+)$', UpdateTipoTurno ,  name='UpdateTipoTurno' ),
	##########################PORCENTAJES####################################
	url(r'^Porcentaje/Nuevo/$', NewPorcentaje , name='NewPorcentaje'  ),
	url(r'^Porcentaje/Get/Registro/$', GetPorcentaje ,  name='GetPorcentaje' ),
	url(r'^Porcentaje/Editar/(?P<id_porcentaje>\d+)$', UpdatePorcentaje, name='UpdatePorcentaje'  ),
	url(r'^Porcentaje/Solicitud/Eliminar/Registro/$', DeletePorcentaje ,  name='DeletePorcentaje' ),
	url(r'^Porcentaje/Get/$', PorcentajesoptionsGet ,  name='PorcentajesoptionsGet' ),
	url(r'^Porcentaje/Solicitud/Get/Registro/$', getDescuento ,  name='getDescuento' ),
	##########################MAILS######################################################
	url(r'^Email/Nuevo/$', NewMail , name='NewMail'  ),
	url(r'^Email/Eliminar/$', DeleteMail , name='DeleteMail'  ),
	url(r'^Email/Get/$', GetMail , name='GetMail'  ),
	url(r'^Email/Update/(?P<id_mail>\d+)$', UpdateMail ,  name='UpdateMail' ),
	#################################TERMINOS####################################
	url(r'^Terminos/Nuevo/$', NewTermino , name='NewTermino'  ),
	url(r'^Terminos/Eliminar/$', DeleteTermino , name='DeleteTermino'  ),
	url(r'^Terminos/Get/$', GetTermino , name='GetTermino'  ),
	url(r'^Terminos/Update/(?P<id_termino>\d+)$', UpdateTermino ,  name='UpdateTermino' ),
	url(r'^Terminos/Enviar/$', enviartermino , name='enviartermino'  ),
	url(r'^Terminos/Solicitud/Get/Registro/$', getTerminoView ,  name='getTerminoView' ),
	url(r'^(?P<id_socio>[0-9]+)/patk/$', recibodeid ,  name='recibodeid' ),

	
]