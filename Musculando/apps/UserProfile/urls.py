from django.conf.urls import url
from django.contrib import admin
from apps.UserProfile.views import ListadoDeUsuarios
from apps.UserProfile.views import Perfil
from apps.UserProfile.views import RegistroUser
from apps.UserProfile.views import RegisterDebug
urlpatterns = [
	#url(r'^registro/$', Registro, name='Registro'  ),
	#url(r'^editar/(?P<id_UserProfile>\d+)$', EditUserProfile, name='EditUserProfile'  ),
	#url(r'^borrar/(?P<id_UserProfile>\d+)$', DeleteUserProfile, name='DeleteUserProfile'  ),
	#url(r'^nuevousuario/$', NuevoUsuario, name='NuevoUsuario'  ),
	#url(r'^nuevoperfil/$', NuevoPerfil, name='NuevoPerfil'  ),
	url(r'^Registro/Nuevo$', RegistroUser , name='RegistroUser'  ),
	url(r'^Lista/$', ListadoDeUsuarios , name='ListadoDeUsuarios'  ),
  	url(r'^Perfil/$', Perfil , name='Perfil'  ),
]