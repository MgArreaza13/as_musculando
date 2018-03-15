from django.conf.urls import url
from django.contrib import admin
#######################PLANES##############################
from apps.Configuracion.views import NuevoPlan
from apps.Configuracion.views import ListaDePlanes
from apps.Configuracion.views import EliminarPlan
from apps.Configuracion.views import getPlan
from apps.Configuracion.views import updatePlan
#from apps.Panel.views import Login
#from apps.Panel.views import ComingSoon
#from apps.Panel.views import Logout


urlpatterns = [
	########################PLANES#########################################
	url(r'^Planes/Lista/$', ListaDePlanes ,  name='ListaDePlanes' ),
	url(r'^Planes/Solicitud/Nuevo/Registro/$', NuevoPlan ,  name='NuevoPlan' ),
	url(r'^Planes/Solicitud/Eliminar/Registro/$', EliminarPlan ,  name='EliminarPlan' ),
	url(r'^Planes/Solicitud/Get/Registro/$', getPlan ,  name='getPlan' ),
	url(r'^Planes/Solicitud/Update/Registro/$', updatePlan ,  name='updatePlan' ),

	#url(r'^$', Inicio, name='Inicio' ),
	#url(r'^Entrar/$', Login, name='Login' ),
	#url(r'^Viene/Pronto$', ComingSoon, name='ComingSoon' ),
	#url(r'^Salir/$', Logout, name='Logout' ),
	#url(r'^calendario/$', calendario, name='calendario' ),
	#url(r'^ingresosegresos/$', ingresosegresos, name='ingresoegresos' ),
	#url(r'^registro/$', registro ),
  
]