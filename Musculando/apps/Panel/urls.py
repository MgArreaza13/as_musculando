from django.conf.urls import url
from django.contrib import admin
from apps.Panel.views import Inicio
from apps.Panel.views import Login
from apps.Panel.views import ComingSoon
from apps.Panel.views import Logout
from apps.Panel.views import ActualizacionUsuario

urlpatterns = [
	url(r'^$', Inicio, name='Inicio' ),
	url(r'^Entrar/$', Login, name='Login' ),
	url(r'^Viene/Pronto$', ComingSoon, name='ComingSoon' ),
	url(r'^Salir/$', Logout, name='Logout' ),
	url(r'^ActualizacionUsuario/$', ActualizacionUsuario, name='ActualizacionUsuario' ),
	#url(r'^ingresosegresos/$', ingresosegresos, name='ingresoegresos' ),
	#url(r'^bloqueado/$', loockscreen ,  name='bloqueado' ),
	#url(r'^registro/$', registro ),
  
]