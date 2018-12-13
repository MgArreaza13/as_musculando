from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
import json
from django.core import serializers
###################MODELS######################
from apps.Canchas.models import Cancha
from apps.Canchas.models import ReservaCancha
from apps.Configuracion.models import tb_turn_sesion
###################Forms######################
from apps.Canchas.forms import CanchaForm
from apps.Canchas.forms import nuevaReservasForm


def NewCancha(request):
	Form = CanchaForm()
	if request.method == 'POST':
		Form = CanchaForm(request.POST, request.FILES  or None)
		if Form.is_valid():
			Form.save()
			return redirect('Canchas:listCanchas')
	contexto = {
		'Form':Form
	}
	return render(request, 'Canchas/Nuevo.html', contexto)



def UpdateCancha(request ,pk):
	cancha = Cancha.objects.get(id = pk)
	if request.method == 'GET':
		Form  = CanchaForm(instance = cancha)
	else:		
		Form  = CanchaForm(request.POST , request.FILES  ,  instance = cancha)
		if Form.is_valid():
			#nuevoPerfil = Form.save(commit=False)
			#if len(request.FILES) != 0:
			#	nuevoPerfil.image = request.FILES['ImagenDePerfil']
			#else:				
			#	nuevoPerfil.image = 'Null'
			Form.save()
			#nuevoColaborador = Form2.save(commit=False)
			#nuevoColaborador.user = tb_profile.objects.get(id = nuevoPerfil.id)
			#nuevoColaborador.save() 
				################ENVIAR CORREO QUE SE CREO EL PERFIL DE SOCIO CORRECTAMENTE ########
#			#NewSocioMAil.delay(request.POST['nameUser'], nuevoSocio.TarifaMensual.precioPlan, nuevoSocio.TarifaMensual.nombrePlan, request.POST['mailUser'])
			return redirect('Canchas:listCanchas')
		else:
		#	#Form	= UsuarioForm(request.POST , request.FILES  or None)
			Form  = CanchaForm(request.POST, request.FILES  or None)
			#Form2 = ColaboradoresRegisterForm(request.POST, request.FILES  or None)
			#fallido = "No pudimos guardar sus datos, intentalo de nuevo luego de verificarlos" 
	return render (request, 'Canchas/Nuevo.html' , {'Form':Form})



def listCanchas(request):
	contexto = {
		'Lista': Cancha.objects.all()
	}
	return render(request, 'Canchas/Lista.html', contexto )



def DeleteCancha(request):
	status 		= None
	id_cancha 	= 	request.GET.get('id_cancha', None)
	cancha  	=	Cancha.objects.get(id = id_cancha)
	cancha.delete()
	status 		=	200
	return HttpResponse(status)



def ReservasWeb(request):
	canchas = Cancha.objects.all()
	turnos 	= ReservaCancha.objects.filter(statusTurn='Confirmada')
	tipe_turnos = tb_turn_sesion.objects.all()
	contexto = {
		'canchas':canchas,
		'turnos':turnos,
		'tipe_turnos':tipe_turnos
	}
	return render(request , 'Canchas/ReservasWeb.html', contexto )



def ReservaWebQueryset(request):
	date = request.GET.get('date', None)
	query = serializers.serialize("json", ReservaCancha.objects.filter(dateTurn = date).filter(statusTurn='Confirmada'))
	return HttpResponse(query)

###################################################################################################
###################################RESERVAS#######################################################


def getReservasList(request):
	reservas 	= ReservaCancha.objects.all()
	context 	= {
		'reservas':reservas
	} 
	return render(request, 'Canchas/ReservasList.html', context)


def updateState(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	pk = body['id']
	content = body['state']
	queryset = ReservaCancha.objects.get(id = pk)
	queryset.statusTurn = content
	queryset.save()
	status = {
		'code':200 ,
		'state':content
	}
	return JsonResponse(status)

def DeleteReserva(request):
	print('entre')
	status 		= None
	print('sigo adentro')
	pk 	= 	request.GET.get('id_reserva', None)
	print('no deberia fallar')
	Reserva  	=	ReservaCancha.objects.get(id = pk)
	Reserva.delete()
	status 		=	200
	return HttpResponse(status)


def updateReservas(request ,pk):
	reserva = ReservaCancha.objects.get(id = pk)
	if request.method == 'GET':
		Form  = nuevaReservasForm(instance = reserva)
	else:		
		Form  = nuevaReservasForm(request.POST , request.FILES  ,  instance = reserva)
		if Form.is_valid():
			Form.save()
			return redirect('Canchas:getReservasList')
		else:
			Form  = nuevaReservasForm(request.POST, request.FILES  or None)
	return render (request, 'Canchas/updateReservas.html' , {'Form':Form})




def getReservasJson(request):
	queryset = ReservaCancha.objects.all().only('cancha', 'dateTurn')
	#reservas = []
	#for reserva in queryset:
	#	new_object = {
	#		'title': reserva.cancha.nameCancha, 
	#		#'start': reserva.dateTurn
	#	}
	#	reservas.append(new_object)
	#print(reservas)
	return JsonResponse(serializers.serialize("json",queryset, fields=('cancha', 'dateTurn')) , safe=False)






def NuevaReservaOnline(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	cancha = Cancha.objects.get( id = body['cancha'] )
	newReserva = ReservaCancha()
	newReserva.mail = body['correo']
	newReserva.nombre = body['nombre']
	newReserva.telefono = body['telefono']
	newReserva.statusTurn =  'En Espera'
	newReserva.turn = tb_turn_sesion.objects.get( id = body['turn'] )
	newReserva.cancha = Cancha.objects.get( id = body['cancha'] )
	newReserva.dateTurn = body['fecha']
	newReserva.montoAPagar = cancha.precioHora

	newReserva.save()
	status = {
		'code':200 ,
	}
	return JsonResponse(status)

def newReserva(request):
	canchas = Cancha.objects.all()
	turnos 	= ReservaCancha.objects.filter(statusTurn='Confirmada')
	tipe_turnos = tb_turn_sesion.objects.all()
	contexto = {
		'canchas':canchas,
		'turnos':turnos,
		'tipe_turnos':tipe_turnos
	}
	return render(request, 'Canchas/ReservasInternas.html', contexto )