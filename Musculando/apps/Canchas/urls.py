from django.conf.urls import url
from django.contrib import admin
from apps.Canchas.views import listCanchas
from apps.Canchas.views import DeleteCancha
from apps.Canchas.views import NewCancha
from apps.Canchas.views import ReservasWeb
from apps.Canchas.views import UpdateCancha
from apps.Canchas.views import getReservasList
from apps.Canchas.views import updateState
from apps.Canchas.views import DeleteReserva
from apps.Canchas.views import updateReservas
from apps.Canchas.views import getReservasJson
from apps.Canchas.views import ReservaWebQueryset
from apps.Canchas.views import NuevaReservaOnline
from apps.Canchas.views import newReserva

urlpatterns = [
	#url(r'^registro/$', Registro, name='Registro'  ),
	#url(r'^editar/(?P<id_UserProfile>\d+)$', EditUserProfile, name='EditUserProfile'  ),
	#url(r'^borrar/(?P<id_UserProfile>\d+)$', DeleteUserProfile, name='DeleteUserProfile'  ),
	#url(r'^nuevousuario/$', NuevoUsuario, name='NuevoUsuario'  ),
	#url(r'^Nuevo/$', Nuevo, name='Nuevo'  ),
	#url(r'^Nueva/Peticion/de/Nuevo/Proveedor$', NuevoProveedor, name='NuevoProveedor'  ),
	url(r'^web/consulta/$', ReservaWebQueryset , name='ReservaWebQueryset'  ),
	url(r'^Lista/$', listCanchas , name='listCanchas'  ),
	url(r'^Nueva/$', NewCancha , name='NewCancha'  ),
	url(r'^Eliminar/Registro$', DeleteCancha , name='DeleteCancha'  ),
	url(r'^Reservas/Web$', ReservasWeb , name='ReservasWeb'  ),
	url(r'^editar/(?P<pk>\d+)$', UpdateCancha, name='UpdateCancha'  ),
	url(r'^Reservas/Lista/$', getReservasList , name='getReservasList'  ),
  	url(r'^Reservas/update/state$', updateState , name='updateState'  ),
  	url(r'^Reservas/get/json/$', getReservasJson , name='getReservasJson'  ),
  	url(r'^Reservas/delete$', DeleteReserva , name='DeleteReserva'  ),
  	url(r'^Reservas/nueva/web$', NuevaReservaOnline , name='NuevaReservaOnline'  ),
  	url(r'^Reservas/Editar/(?P<pk>\d+)$', updateReservas, name='updateReservas'  ),
  	url(r'^Reservas/$', newReserva, name='newReserva'  ),
]