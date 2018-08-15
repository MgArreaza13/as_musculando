from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core import serializers
#####################MODELOS##########################
from apps.Colaboradores.models import tb_colaboradores
from apps.UserProfile.models import tb_profile
from apps.Configuracion.models import tb_tipoColaborador
from apps.Colaboradores.models import tb_cuentaColaborador
from apps.Colaboradores.models import tb_EntradaSalida
from apps.Caja.models import tb_egreso
from apps.Configuracion.models import tb_tipoEgreso
#####################FORMS#############################
from apps.Colaboradores.forms import ColaboradoresRegisterForm
from apps.UserProfile.forms import ProfileForm
from apps.UserProfile.forms import UsuarioForm
#####################TAREAS############################
from apps.tasks.Email_tasks import ColaboradorEliminado
from apps.tasks.Email_tasks import PagoColaborador
from apps.tasks.Email_tasks import PresentimoColaborador
from apps.Colaboradores.tasks import LiquidacionColaboradores
from apps.Colaboradores.tasks import presentimo
#####################utilidades#########################
from django.db.models import Count, Min, Sum, Avg



# Create your views here.
@login_required(login_url = 'Panel:Login' )
def ListEntradaSalida(request):
	list_entrada = tb_EntradaSalida.objects.all()
	contexto = {
		'list_entrada':list_entrada
	}
	return render(request, 'Colaboradores/listaEntradaSalida.html', contexto )


def EntradaSalida(request):
	usuario = request.GET.get('usuario', None)
	password = request.GET.get('password', None)
	entrada_salida = request.GET.get('entradaSalida_', None)
	user 	= authenticate(username=usuario, password=password)
	status = 503
	if user != None:
		new_object = tb_EntradaSalida()
		new_object.colaborador = tb_colaboradores.objects.get(user__user__id = user.id)
		new_object.typeEntradaSalida = entrada_salida
		new_object.save()
		status =  200
	
	return HttpResponse(status)




def ProcesarLiquidacion(request):
	id_colaborador = request.GET.get('id', None)
	pagar_presentimo = request.GET.get('pagar_presentimo', None)
	abono = float(request.GET.get('abono', None))
	colaborador = tb_colaboradores.objects.get(id = id_colaborador)
	colaborador.montoPagadoColaborador += abono
	colaborador.cuentaColaborador -= abono
	colaborador.isHonorariosUpload = False
	colaborador.save()
	PagoColaborador.delay(colaborador.user.nameUser, colaborador.user.mailUser)
	egreso = tb_egreso()
	egreso.user = request.user
	egreso.monto = abono
	egreso.descripcion = 'Pago de Colaborador'
	egreso.tipoDeEgreso = tb_tipoEgreso.objects.get(  tipodeEgreso = 'Pago Colaboradores')
	egreso.colaborador = tb_colaboradores.objects.get(id = id_colaborador)
	egreso.save()
	if pagar_presentimo == 'Si' and colaborador.isPresentimoPay == False:
		colaborador = tb_colaboradores.objects.get(id = id_colaborador)
		colaborador.montoPagadoColaborador += colaborador.presentimo
		colaborador.isPresentimoPay = True
		colaborador.save()
		PresentimoColaborador.delay(colaborador.user.nameUser, colaborador.user.mailUser)
		egreso = tb_egreso()
		egreso.user = request.user
		egreso.monto = colaborador.presentimo
		egreso.descripcion = 'Pago de Colaborador - Presentimo'
		egreso.tipoDeEgreso = tb_tipoEgreso.objects.get(  tipodeEgreso = 'Pago Colaboradores')
		egreso.colaborador = tb_colaboradores.objects.get(id = id_colaborador)
		egreso.save()
	status = 200
	return HttpResponse(status)


def getColaborador(request):
	id_colaborador = request.GET.get('id', None)
	colaborador = tb_colaboradores.objects.filter(id = id_colaborador)
	data = serializers.serialize("json", colaborador)
	return HttpResponse(data)




@login_required(login_url = 'Panel:Login' )
def CuentaColaborador(request, id_colaborador):
	colaborador = tb_colaboradores.objects.get(id = id_colaborador)
	list_cuenta = tb_cuentaColaborador.objects.filter(colaborador__id = id_colaborador)
	pagos_realizados = tb_egreso.objects.filter(colaborador__id = id_colaborador)
	total_pagos_realizados = tb_egreso.objects.filter(colaborador__id = id_colaborador).aggregate(total=Sum('monto'))
	monto_total_de_cuenta = tb_cuentaColaborador.objects.filter(colaborador__id = id_colaborador).aggregate(total=Sum('monto'))
	if monto_total_de_cuenta['total'] != None  and total_pagos_realizados['total'] != None:
		total_deudas_por_pagar = float(monto_total_de_cuenta['total']) - float(total_pagos_realizados['total'])
	elif monto_total_de_cuenta['total'] != None and total_pagos_realizados['total'] == None:
		total_deudas_por_pagar = float(monto_total_de_cuenta['total']) 
	else:
		total_deudas_por_pagar = 0 
	context = {
		'colaborador':colaborador,
		'list_cuenta':list_cuenta,
		'pagos_realizados':pagos_realizados,
		'total_pagos_realizados':total_pagos_realizados,
		'monto_total_de_cuenta':monto_total_de_cuenta,
		'total_deudas_por_pagar':total_deudas_por_pagar
	}
	return render(request, 'Colaboradores/Cuenta.html', context )










def ProcesoDeLiquidacion(request):
	status = 200 
	id_u =  request.user.id
	LiquidacionColaboradores.delay(id_u)
	return HttpResponse(status)






@login_required(login_url = 'Panel:Login' )
def ListaDeColaboradores(request):
	Colaboradores = tb_colaboradores.objects.all()
	monto_total = tb_colaboradores.objects.all().aggregate(total=Sum('cuentaColaborador'))
	contexto = {
		'Colaboradores':Colaboradores,
		'monto_total':monto_total
	}
	return render(request, 'Colaboradores/Liquidacion.html', contexto)


def EliminarColaborador(request):
	status = None
	id_colaborador = request.GET.get('id', None)
	id_profile = request.GET.get('id_profile', None)
	queryset = tb_colaboradores.objects.get(id = id_colaborador)
	ColaboradorEliminado.delay()
	queryset.delete()
	queryset2 = tb_profile.objects.get(id = id_profile)
	queryset2.delete()
	status = 200
	return HttpResponse(status)

@login_required(login_url = 'Panel:Login' )
def NewColaborador(request):
	Form = UsuarioForm()
	Form2 = ProfileForm()
	Form3 = ColaboradoresRegisterForm()
	fallido = None
	if request.method == 'POST':
		Form = UsuarioForm(request.POST, request.FILES  or None)
		Form2 = ProfileForm(request.POST, request.FILES  or None)
		Form3 = ColaboradoresRegisterForm(request.POST, request.FILES  or None)
		if Form.is_valid() and Form2.is_valid() and Form3.is_valid():
			Form.save()
			usuario = request.POST['username']
			clave 	= request.POST['password1']
			user 	= authenticate(username=usuario, password=clave)
			if user is not None and user.is_active:
				nuevoPerfil = tb_profile()
				nuevoPerfil.user = user
				nuevoPerfil.nameUser = request.POST['nameUser']
				nuevoPerfil.lastName = request.POST['lastName']
				nuevoPerfil.dni = request.POST['dni']
				nuevoPerfil.movilTlf = request.POST['movilTlf']
				nuevoPerfil.houseTlf = request.POST['houseTlf']
				nuevoPerfil.mailUser = request.POST['mailUser']
				nuevoPerfil.tipoUser = 'Colaborador'
				if len(request.FILES) != 0:
					nuevoPerfil.image = request.FILES['ImagenDePerfil']
				else:
					nuevoPerfil.image = 'Null'
				nuevoPerfil.save()
				nuevoColaborador = Form3.save(commit=False)
				nuevoColaborador.user = tb_profile.objects.get(id = nuevoPerfil.id)
				nuevoColaborador.cuentaColaborador = request.POST['honorariosMensuales']
				nuevoColaborador.save() 
				#luego de guardar, necesito registrar el ingreso principal del colaborador
				if float(request.POST['honorariosMensuales']) != 0 :
					cuenta = tb_cuentaColaborador()
					cuenta.colaborador = tb_colaboradores.objects.get(id = nuevoColaborador.id)
					cuenta.typePago = 'Honorarios Mensual'
					cuenta.monto = float(request.POST['honorariosMensuales'])
					cuenta.save() 
				return redirect('Colaboradores:ListaDeColaboradores')
		else:
			Form = UsuarioForm(request.POST, request.FILES  or None)
			Form2 = ProfileForm(request.POST, request.FILES  or None)
			Form3 = ColaboradoresRegisterForm(request.POST, request.FILES  or None)
			fallido = "No pudimos guardar sus datos, intentalo de nuevo luego de verificarlos" 
	contexto = {
	'Form':Form,
	'Form2':Form2,
	'Form3':Form3,
	'fallido':fallido,
	}
	return render(request, 'Colaboradores/nuevo.html' , contexto)

@login_required(login_url = 'Panel:Login' )
def UpdateColaboradores(request , id_colaborador):
	colaborador= tb_colaboradores.objects.get(id = id_colaborador)
	perfil = tb_profile.objects.get(id = colaborador.user.id)
	fallido = None	
	if request.method == 'GET':
		Form  = ProfileForm(instance = perfil)
		Form2 = ColaboradoresRegisterForm(instance = colaborador)
	else:		
		Form  = ProfileForm(request.POST , request.FILES  ,  instance = perfil)
		Form2 = ColaboradoresRegisterForm(request.POST , request.FILES  ,  instance = colaborador)
		if Form.is_valid() and Form2.is_valid():
			nuevoPerfil = Form.save(commit=False)
#			#nuevoPerfil.user = 
			nuevoPerfil.nameUser = request.POST['nameUser']
			nuevoPerfil.lastName = request.POST['lastName']
			nuevoPerfil.dni = request.POST['dni']
			nuevoPerfil.movilTlf = request.POST['movilTlf']
			nuevoPerfil.houseTlf = request.POST['houseTlf']
			nuevoPerfil.mailUser = request.POST['mailUser']
			nuevoPerfil.tipoUser = 'Colaborador'
			if len(request.FILES) != 0:
				nuevoPerfil.image = request.FILES['ImagenDePerfil']
			else:				
				nuevoPerfil.image = 'Null'
			nuevoPerfil.save()
			nuevoColaborador = Form2.save(commit=False)
			nuevoColaborador.user = tb_profile.objects.get(id = nuevoPerfil.id)
			nuevoColaborador.save() 
				################ENVIAR CORREO QUE SE CREO EL PERFIL DE SOCIO CORRECTAMENTE ########
#			#NewSocioMAil.delay(request.POST['nameUser'], nuevoSocio.TarifaMensual.precioPlan, nuevoSocio.TarifaMensual.nombrePlan, request.POST['mailUser'])
			return redirect('Colaboradores:ListaDeColaboradores')
		else:
		#	#Form	= UsuarioForm(request.POST , request.FILES  or None)
			Form  = ProfileForm(request.POST, request.FILES  or None)
			Form2 = ColaboradoresRegisterForm(request.POST, request.FILES  or None)
			fallido = "No pudimos guardar sus datos, intentalo de nuevo luego de verificarlos" 
	return render (request, 'Colaboradores/nuevo.html' , {'Form':Form,'Form2':Form2,'fallido':fallido,})
