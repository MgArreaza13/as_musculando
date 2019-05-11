from django.shortcuts import render, redirect
import json
from apps.Scripts.validatePerfil import validatePerfil
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
###############MODELOS################
from apps.Configuracion.models import tb_termino
from apps.Configuracion.models import tb_plan
from apps.Configuracion.models import tb_plan_diario
from apps.Configuracion.models import tb_formasDePago
from apps.Configuracion.models import tb_tipoColaborador
from apps.Configuracion.models import tb_tipoEgreso
from apps.Configuracion.models import tb_tipoIngreso
from apps.Socios.models import tb_socio
from apps.Configuracion.models import tb_turn_sesion
from apps.Configuracion.models import tb_porcentaje
from apps.UserProfile.models import tb_profile
from apps.UserProfile.models import tb_profile
from apps.Configuracion.models import tb_mailsAdministrador
##############FORMULARIOS################
from apps.Configuracion.forms import PlanRegisterForm
from apps.Configuracion.forms import PorcentajeRegisterForm
from apps.Configuracion.forms import tipoTurnForm
from apps.Configuracion.forms import EmailRegisterForm
from apps.Configuracion.forms import TerminoRegisterForm
from apps.tasks.Email_tasks import Enviartermino
# Create your views here.
#import datetime
import time

############################PLANES#####################################
@login_required(login_url = 'Panel:Login' )
def ListaDePlanes(request):
	planes = tb_plan.objects.all()
	contexto = {
	'planes':planes
	}
	return render(request, 'Configuracion/Planes/ListadoDePlanes.html', contexto )



def NuevoPlan(request):
	status = None
	titulo = request.GET.get('Nombre', None)
	precio = request.GET.get('Precio', None)
	precioAnual = request.GET.get('PrecioAnual', None)
	descripcion = request.GET.get('Descripcion', None)
	queryset =  tb_plan.objects.filter(nombrePlan = titulo)
	if(len(queryset)>=1):
		status = 400
	else:
		new_plan = tb_plan()
		new_plan.user = request.user
		new_plan.nombrePlan = titulo
		new_plan.precioPlan = precio 
		new_plan.descripcionPlan = descripcion
		new_plan.precioPlanAnual = precioAnual
		new_plan.save()
		status = 200
	return HttpResponse(status)


@login_required(login_url = 'Panel:Login' )
def ListaDePlanes_diarios(request):
	planes_diarios = tb_plan_diario.objects.all()
	contexto = {
	'planes_diarios':planes_diarios
	}
	return render(request, 'Configuracion/Planes/ListadoDePlanesDiarios.html', contexto )

def NuevoPlanDiario(request):
	status = None
	titulo = request.GET.get('Nombre', None)
	precio = request.GET.get('Precio', None)
	descripcion = request.GET.get('Descripcion', None)
	queryset =  tb_plan_diario.objects.filter(nombrePlan = titulo)
	if(len(queryset)>=1):
		status = 400
	else:
		new_plan = tb_plan_diario()
		new_plan.user = request.user
		new_plan.nombrePlan = titulo
		new_plan.precioPlan = precio 
		new_plan.descripcionPlan = descripcion
		new_plan.save()
		status = 200
	return HttpResponse(status)

def EliminarPlanDiario(request):
	status = None
	id_plan = request.GET.get('id', None)
	queryset = tb_plan_diario.objects.get(id=id_plan)
	queryset.delete()
	status = 200
	return HttpResponse(status)

def EliminarPlan(request):
	status = None
	id_plan = request.GET.get('id', None)
	queryset = tb_plan.objects.get(id=id_plan)
	queryset.delete()
	status = 200
	return HttpResponse(status)

def getPlan(request):
	id_plan = request.GET.get('id', None)
	queryset = tb_plan.objects.get(id= id_plan)
	plan = {
		'nombrePlan':queryset.nombrePlan,
		'precioPlan':queryset.precioPlan,
		'montoAnal':queryset.precioPlanAnual,
		'descripcionPlan':queryset.descripcionPlan,
		'user':str(queryset.user),
		'fecha':queryset.dateCreate,
	}
	return JsonResponse(plan)

def updatePlan(request):
	status = None
	id_plan = request.GET.get('id', None)
	titulo = request.GET.get('Nombre', None)
	precio = request.GET.get('Precio', None)
	PrecioAnual = request.GET.get('MontoAnual', None)
	descripcion = request.GET.get('Descripcion', None)
	queryset =  tb_plan.objects.get(id = id_plan)
	queryset.nombrePlan = titulo
	queryset.precioPlan = precio 
	queryset.precioPlanAnual = PrecioAnual
	queryset.descripcionPlan = descripcion
	queryset.save()
	status = 200
	return HttpResponse(status)

def getPlanDiario(request):
	id_plan = request.GET.get('id', None)
	queryset = tb_plan_diario.objects.get(id= id_plan)
	plan = {
		'nombrePlan':queryset.nombrePlan,
		'precioPlan':queryset.precioPlan,
		'descripcionPlan':queryset.descripcionPlan,
		'user':str(queryset.user),
		'fecha':queryset.dateCreate,
	}
	return JsonResponse(plan)

def updatePlanDiario(request):
	status = None
	id_plan = request.GET.get('id', None)
	titulo = request.GET.get('Nombre', None)
	precio = request.GET.get('Precio', None)
	PrecioAnual = request.GET.get('MontoAnual', None)
	descripcion = request.GET.get('Descripcion', None)
	queryset =  tb_plan_diario.objects.get(id = id_plan)
	queryset.nombrePlan = titulo
	queryset.precioPlan = precio 
	queryset.descripcionPlan = descripcion
	queryset.save()
	status = 200
	return HttpResponse(status)

################################CONFIGURACION GENERAL###############################
def Configuracion_g(request):
	formas_de_pago 			= tb_formasDePago.objects.all()
	tipos_de_colaboradores  = tb_tipoColaborador.objects.all()
	tipos_de_egresos		= tb_tipoEgreso.objects.all()
	tipos_de_ingresos		= tb_tipoIngreso.objects.all()
	tipos_de_turnos			= tb_turn_sesion.objects.all()
	porcentajes				= tb_porcentaje.objects.all()
	emails 					= tb_mailsAdministrador.objects.all()
	terminos 				= tb_termino.objects.all()
	contexto = {
	'formas_de_pago':formas_de_pago,
	'tipos_de_colaboradores':tipos_de_colaboradores,
	'tipos_de_egresos':tipos_de_egresos,
	'tipos_de_ingresos':tipos_de_ingresos,
	'tipos_de_turnos':tipos_de_turnos,
	'porcentajes':porcentajes,
	'emails':emails,
	'terminos':terminos,
	} 
	return render(request, 'Configuracion/Configuracion_General.html', contexto)



################################FORMA DE PAGOS ######################################

def DeleteFormadePago(request):
	status = None
	id_forma_de_pago = request.GET.get('id', None)
	queryset = tb_formasDePago.objects.get(id=id_forma_de_pago)
	queryset.delete()
	status = 200
	return HttpResponse(status)


def NewFormadePago(request):
	status = None
	formadepago = request.GET.get('nombreFormaPago', None)
	queryset = tb_formasDePago.objects.filter(nameFormasDePago = formadepago )
	if (len(queryset) >= 1):
		status = 401
	else:
		formadepago_model = tb_formasDePago()
		formadepago_model.user = request.user
		formadepago_model.nameFormasDePago =  formadepago
		formadepago_model.save()
		status = 200
	return HttpResponse(status)

def GetFormaDePago(request):
	id_forma_de_pago = request.GET.get('id_forma_de_pago', None)
	queryset = tb_formasDePago.objects.get(id= id_forma_de_pago)
	formaDePago = {
		'user':str(queryset.user),
		'formaDePago':queryset.nameFormasDePago,
	}
	return JsonResponse(formaDePago)


def UpdateFormaDePago(request):
	id_forma_de_pago = request.GET.get('id_forma_de_pago', None)
	queryset = tb_formasDePago.objects.get(id= id_forma_de_pago)
	queryset.user = request.user
	queryset.nameFormasDePago = request.GET.get('nombreFormaPago', None)
	queryset.save()
	status = 200 
	return HttpResponse(status)


def FormasdePagoGet(request):
	formas_de_pago = tb_formasDePago.objects.all()
	lista = [{'id': pago.id, 'forma_de_pago': pago.nameFormasDePago} for pago in formas_de_pago]
	data = json.dumps(lista)
	

	return HttpResponse(data)







################################TIPOS DE COLABORADORES######################################



def NuevoTipoDeColaborador(request):
	status = None
	tipo_de_colaborador = request.GET.get('TipoDeColaborador', None)
	queryset = tb_tipoColaborador.objects.filter(tipodeColaborador = tipo_de_colaborador )
	if (len(queryset) >= 1):
		status = 401
	else:
		tipo = tb_tipoColaborador()
		tipo.user = request.user
		tipo.tipodeColaborador =  tipo_de_colaborador
		tipo.save()
		status = 200
	return HttpResponse(status)





def DeleteTipoDeColaborador(request):
	status = None
	id_tipo_de_colaborador = request.GET.get('id', None)
	queryset = tb_tipoColaborador.objects.get(id=id_tipo_de_colaborador)
	queryset.delete()
	status = 200
	return HttpResponse(status)




def GetTipoColaborador(request):
	id_tipo_de_colaborador = request.GET.get('id_tipo_colaborador', None)
	queryset = tb_tipoColaborador.objects.get(id = id_tipo_de_colaborador)
	print(queryset)
	tipo_colaborador = {
		'user':str(queryset.user),
		'tipodecolaborador':queryset.tipodeColaborador,
	}
	return JsonResponse(tipo_colaborador)




def UpdateTipoColaborador(request):
	id_tipo_colaborador = request.GET.get('id_tipo_colaborador', None)
	queryset = tb_tipoColaborador.objects.get(id= id_tipo_colaborador)
	queryset.user = request.user
	queryset.tipodeColaborador = request.GET.get('nombre_tipo_colaborador', None)
	queryset.save()
	status = 200 
	return HttpResponse(status)



######################################TIPOS DE EGRESOS#############################################



def NuevoTipoDeEgreso(request):
	status = None
	tipo_de_egreso = request.GET.get('TipoDeEgreso', None)
	queryset = tb_tipoEgreso.objects.filter(tipodeEgreso = tipo_de_egreso )
	if (len(queryset) >= 1):
		status = 401
	else:
		tipo = tb_tipoEgreso()
		tipo.user = request.user
		tipo.tipodeEgreso =  tipo_de_egreso
		tipo.save()
		status = 200
	return HttpResponse(status)


def DeleteTipoDeEgreso(request):
	status = None
	id_tipo_de_egreso = request.GET.get('id', None)
	queryset = tb_tipoEgreso.objects.get(id=id_tipo_de_egreso)
	queryset.delete()
	status = 200
	return HttpResponse(status)


def GetTipoEgreso(request):
	id_tipo_de_egreso = request.GET.get('id_tipo_egreso', None)
	queryset = tb_tipoEgreso.objects.get(id = id_tipo_de_egreso)
	tipo_egreso = {
		'user':str(queryset.user),
		'tipodeEgreso':queryset.tipodeEgreso,
	}
	return JsonResponse(tipo_egreso)




def UpdateTipoEgreso(request):
	id_tipo_de_egreso = request.GET.get('id_tipo_egreso', None)
	queryset = tb_tipoEgreso.objects.get(id = id_tipo_de_egreso)
	queryset.user = request.user
	queryset.tipodeEgreso = request.GET.get('nombre_tipo_egreso', None)
	queryset.save()
	status = 200 
	return HttpResponse(status)




######################################TIPOS DE INGRESOS#############################################



def NuevoTipoDeIngreso(request):
	status = None
	tipo_de_ingreso = request.GET.get('TipoDeIngreso', None)
	queryset = tb_tipoIngreso.objects.filter(tipodeIngreso = tipo_de_ingreso )
	if (len(queryset) >= 1):
		status = 401
	else:
		tipo = tb_tipoIngreso()
		tipo.user = request.user
		tipo.tipodeIngreso =  tipo_de_ingreso
		tipo.save()
		status = 200
	return HttpResponse(status)


def DeleteTipoDeIngreso(request):
	status = None
	id_tipo_de_ingreso = request.GET.get('id', None)
	queryset = tb_tipoIngreso.objects.get(id=id_tipo_de_ingreso)
	queryset.delete()
	status = 200
	return HttpResponse(status)


def GetTipoIngreso(request):
	id_tipo_de_ingreso = request.GET.get('id_tipo_ingreso', None)
	queryset = tb_tipoIngreso.objects.get(id = id_tipo_de_ingreso)
	tipo_ingreso = {
		'user':str(queryset.user),
		'tipodeIngreso':queryset.tipodeIngreso,
	}
	return JsonResponse(tipo_ingreso)




def UpdateTipoIngreso(request):
	id_tipo_de_ingreso = request.GET.get('id_tipo_ingreso', None)
	queryset = tb_tipoIngreso.objects.get(id = id_tipo_de_ingreso)
	queryset.user = request.user
	queryset.tipodeIngreso = request.GET.get('nombre_tipo_ingreso', None)
	queryset.save()
	status = 200 
	return HttpResponse(status)

###########################HORARIOS######################
def NuevoTipoTurno(request):
	Form = tipoTurnForm
	formato = "%H:%M"
	queryset = tb_turn_sesion.objects.all()
	band = False #hay que declarar una bandera para saber luego que finalice el recorrido si guardar o no 
	if request.method == 'POST':
		Form = tipoTurnForm(request.POST or None)
		if Form.is_valid():
			print('formulario valido')
			#### i el formulario es valido aqui tenemos que hacer la otra vaidacion .
			for objeto in queryset:
				print(objeto)
				#objecto es valga la redundancia el objecto en el cual tu podras ver cada popiedad de cada objecto guardado en tipo de horarios
				#entonces seria algo como
				print(objeto.HoraTurnEnd)
				print(objeto.HoraTurn)
				print(request.POST['TimeTurnStart'])
				if(objeto.HoraTurn.strftime(formato) == request.POST['TimeTurnStart'] ):
					print('encontre una coincidencia ')
					# la hora que intetas gardar esta en el rango de ese objeto
				
					band = True
			print(band)
			if( band == False): #quiere decir que no consiguio ningun problema entonces guardo 
				print('deeria guardar')
				tipoTurno = Form.save(commit=False)
				tipoTurno.user = request.user
				tipoTurno.HoraTurn= request.POST['TimeTurnStart']
				tipoTurno.HoraTurnEnd = request.POST['TimeTurnEnd']
				tipoTurno.save()
				return redirect('Configuracion:Configuracion_g')
			else: #hubo un error
				print('no guardare') 
				mensaje = "Ud esta ingresando un turno ya registrado en el sistema, intente otro."
				return render(request, 'Configuracion/Turnos/NuevoTipoTurno.html' , {'Form':Form, 'mensaje':mensaje})
		else:
			Form = tipoTurnForm()
	return render(request, 'Configuracion/Turnos/NuevoTipoTurno.html' , {'Form':Form})


def DeleteTipoDeTurno(request):
	status = None
	id_tipo_de_turno = request.GET.get('id', None)
	queryset = tb_turn_sesion.objects.get(id=id_tipo_de_turno)
	queryset.delete()
	status = 200
	return HttpResponse(status)

def GetTipoTurno(request):
	id_tipo_de_turno = request.GET.get('id_tipo_de_turno', None)
	queryset = tb_turn_sesion.objects.get(id = id_tipo_de_turno)
	tipo_turno = {
		'user':str(queryset.user),
		'tipo_turno':queryset.nameturnsession,
	}
	return JsonResponse(tipo_turno)

def UpdateTipoTurno(request, id_tipo_de_turno):
	tipeTurnoEditar= tb_turn_sesion.objects.get(id=id_tipo_de_turno)
	if request.method == 'GET':
		Form= tipoTurnForm(instance = tipeTurnoEditar)
	else:
		Form = tipoTurnForm(request.POST, instance = tipeTurnoEditar)
		if Form.is_valid():
			tipoTurno = Form.save(commit=False)
			tipoTurno.user = request.user
			tipoTurno.HoraTurn= request.POST['TimeTurnStart']
			tipoTurno.HoraTurnEnd = request.POST['TimeTurnEnd']
			tipoTurno.save()
			return redirect ('Configuracion:Configuracion_g')
	return render (request, 'Configuracion/Turnos/NuevoTipoTurno.html' , {'Form':Form})

###########################PORCENTAJES######################
def NewPorcentaje(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	Form = PorcentajeRegisterForm()
	if request.method == 'POST':
		Form = PorcentajeRegisterForm(request.POST or None)
		if Form.is_valid():
			Porcentaje = Form.save(commit=False)
			Porcentaje.user = request.user
			Porcentaje.save()
			return redirect('Configuracion:Configuracion_g')
		else:
			print('error')
			
	contexto = {
		'Form': Form,
		'perfil':perfil,
	}
	return render (request, 'Configuracion/Porcentajes/nuevoporcentaje.html', contexto)

def GetPorcentaje(request):
	porcentaje = request.GET.get('id_porcentaje', None)
	queryset = tb_porcentaje.objects.get(id = id_porcentaje)
	data = {
		'user':str(queryset.user),
		'porcentaje':queryset.titulo,
	}
	return JsonResponse(data)

def UpdatePorcentaje(request, id_porcentaje):
	porcentajeEditar= tb_porcentaje.objects.get(id=id_porcentaje)
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	if request.method == 'GET':
		Form= PorcentajeRegisterForm(instance = porcentajeEditar)
	else:
		Form = PorcentajeRegisterForm(request.POST, instance = porcentajeEditar)
		if Form.is_valid():
			porcentaje = Form.save(commit=False)
			porcentaje.user = request.user
			porcentaje.porcentaje= request.POST['porcentaje']
			porcentaje.descripcion = request.POST['descripcion']
			porcentaje.save()
			return redirect ('Configuracion:Configuracion_g')
	return render (request, 'Configuracion/Porcentajes/nuevoporcentaje.html' , {'Form':Form, 'perfil':perfil})


def DeletePorcentaje(request):
	status = None
	id_porcentaje = request.GET.get('id', None)
	queryset = tb_porcentaje.objects.get(id=id_porcentaje)
	queryset.delete()
	status = 200
	return HttpResponse(status)

def PorcentajesoptionsGet(request):
	porcentajes = tb_porcentaje.objects.all()
	lista = [{'id': porcentaje.id, 'porcentajesop': porcentaje.porcentaje} for porcentaje in porcentajes]
	data = json.dumps(lista)
	
	return HttpResponse(data)


def getDescuento(request):
	id_descuento = request.GET.get('id', None)
	queryset = tb_porcentaje.objects.get(id= id_descuento)
	descuento = {
		'descuento':queryset.porcentaje,
		'descripcion':queryset.descripcion,
		
	}
	return JsonResponse(descuento)

############################MAILS#############################
# def NewMail(request):
# 	status = None
# 	nuevo_mail = request.GET.get('nuevo_mail', None)
# 	queryset = tb_mailsAdministrador.objects.filter(mail = nuevo_mail )
# 	if (len(queryset) >= 1):
# 		status = 401
# 	else:
# 		new = tb_mailsAdministrador()
# 		new.user = request.user
# 		new.mail =  nuevo_mail
# 		new.save()
# 		status = 200
# 	return HttpResponse(status)


def DeleteMail(request):
	status = None
	id_mail = request.GET.get('id', None)
	queryset = tb_mailsAdministrador.objects.get(id=id_mail)
	print(queryset)
	queryset.delete()
	status = 200
	return HttpResponse(status)


def NewMail(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	Form = EmailRegisterForm()
	if request.method == 'POST':
		Form = EmailRegisterForm(request.POST or None)
		if Form.is_valid():
			mail = Form.save(commit=False)
			mail.user = request.user
			mail.save()
			return redirect('Configuracion:Configuracion_g')
		else:
			print('error')
			
	contexto = {
		'Form': Form,
		'perfil':perfil,
	}
	return render (request, 'Configuracion/Emails/newemail.html', contexto)

def GetMail(request):
	mail = request.GET.get('id_mail', None)
	queryset = tb_mailsAdministrador.objects.get(id = id_mail)
	data = {
		'user':str(queryset.user),
		'mail':queryset.mail,
	}
	return JsonResponse(data)

def UpdateMail(request, id_mail):
	mailEditar= tb_mailsAdministrador.objects.get(id=id_mail)
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	if request.method == 'GET':
		Form= EmailRegisterForm(instance = mailEditar)
	else:
		Form = EmailRegisterForm(request.POST, instance = mailEditar)
		if Form.is_valid():
			mail = Form.save(commit=False)
			mail.user = request.user
			mail.mail= request.POST['mail']
			mail.save()
			return redirect ('Configuracion:Configuracion_g')
	return render (request, 'Configuracion/Emails/newemail.html' , {'Form':Form, 'perfil':perfil})


############################TERMINOS#############################



def DeleteTermino(request):
	status = None
	id_termino = request.GET.get('id', None)
	queryset = tb_termino.objects.get(id=id_termino)
	print(queryset)
	queryset.delete()
	status = 200
	return HttpResponse(status)


def NewTermino(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	Form = TerminoRegisterForm()
	if request.method == 'POST':
		Form = TerminoRegisterForm(request.POST or None)
		if Form.is_valid():
			mail = Form.save(commit=False)
			mail.user = request.user
			mail.save()
			return redirect('Configuracion:Configuracion_g')
		else:
			print('error')
			
	contexto = {
		'Form': Form,
		'perfil':perfil,
	}
	return render (request, 'Configuracion/Terminos/newTermino.html', contexto)

def GetTermino(request):
	mail = request.GET.get('id_termino', None)
	queryset = tb_termino.objects.get(id = id_termino)
	data = {
		'user':str(queryset.user),
		'nameTerminos':queryset.nameTerminos,

	}
	return JsonResponse(data)

def UpdateTermino(request, id_termino):
	terminoEditar= tb_termino.objects.get(id=id_termino)
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	if request.method == 'GET':
		Form= TerminoRegisterForm(instance = terminoEditar)
	else:
		Form = TerminoRegisterForm(request.POST, instance = terminoEditar)
		if Form.is_valid():
			termino = Form.save(commit=False)
			termino.user = request.user
			termino.nameTerminos= request.POST['nameTerminos']
			termino.save()
			return redirect ('Configuracion:Configuracion_g')
	return render (request, 'Configuracion/Terminos/newTermino.html', {'Form':Form, 'perfil':perfil})


def getTerminoView(request):
	id_termino = request.GET.get('id', None)
	queryset = tb_termino.objects.get(id= id_termino)
	termino = {
		'nameTerminos':queryset.nameTerminos,
		'descripcion':queryset.descripcion,
		
	}
	return JsonResponse(termino)

def enviartermino(request):
	status = None
	id_termino = request.GET.get('id', None)
	queryset = tb_termino.objects.get(id=id_termino)
	print(queryset)
	server = 'http://localhost:8000'
	Enviartermino.delay(queryset.nameTerminos,queryset.descripcion,server)
	status = 200
	return HttpResponse(status)

def recibodeid(request, id_socio):
	socio = tb_socio.objects.get(id=id_socio)
	if socio.AcceptTerms == True:
		return render (request, 'Configuracion/Terminos/404.html')
	else:
		socio.AcceptTerms = True
		socio.save()
	print(id_socio)
	return render (request, 'Configuracion/Terminos/aqui.html')

