from django.conf.urls import url
from django.contrib import admin
from apps.Panel.views import Inicio
from apps.Panel.views import Login



urlpatterns = [
	url(r'^$', Inicio, name='Inicio' ),
	url(r'^entrar/$', Login, name='Login' ),
	#url(r'^salir/$', logout, name='logout' ),
	#url(r'^calendario/$', calendario, name='calendario' ),
	#url(r'^ingresosegresos/$', ingresosegresos, name='ingresoegresos' ),
	#url(r'^bloqueado/$', loockscreen ,  name='bloqueado' ),
	#url(r'^registro/$', registro ),
  
]