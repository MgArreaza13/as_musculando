from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime
########Modelos################
from apps.Socios.models import tb_socio
from apps.Configuracion.models import tb_plan
from apps.Configuracion.models import tb_tipoIngreso
from apps.Configuracion.models import tb_plan_diario
from apps.Configuracion.models import tb_formasDePago
from apps.Configuracion.models import tb_porcentaje
from django.contrib.auth.models import User ##MODULE LO USUARIO DE DJANGO
from apps.Caja.models import tb_ingreso_mensualidad
from apps.Caja.models import tb_ingresos
from apps.UserProfile.models import tb_profile
#######FORMULARIOS#############
from apps.UserProfile.forms import UsuarioForm
from apps.UserProfile.forms import ProfileForm
from apps.Socios.forms import SociosRegisterForm
from apps.Socios.forms import PlanUpdateForm


##########SCRIPTS################
from apps.Scripts.DesactivateUser import Desactivate_Register


######################CELERY################
from apps.tasks.Email_tasks import VencimientoMensualidad
from apps.tasks.Email_tasks import NewSocioMAil
from apps.tasks.Email_tasks import DesactivacionSocio
from apps.tasks.Email_tasks import ActivacionSocio
from apps.tasks.Email_tasks import PerfilEliminado
from apps.tasks.Email_tasks import GetProfile
from apps.tasks.Email_tasks import Testcorreo






# Create your views here.



##########################DATOS DEL SOCIO ########################################

def getSocio(request):
	id_User = request.GET.get('id_socio', None)
	usuario = User.objects.get(id = id_User)
	perfil = tb_profile.objects.get(user__id = id_User)
	socio = tb_socio.objects.get(perfil__user__id = id_User)
	data = {
		'username':str(usuario),
		'name': str(perfil.nameUser),
		'lastname': str(perfil.lastName),
		'mail':str(perfil.mailUser),
		'plan':str(socio.TarifaMensual.nombrePlan),
		'monto_plan':str(socio.TarifaMensual.precioPlan)

	}

	return JsonResponse(data)


#####################FUNCION QUE DESACTIVA SOCIOS POR VENCIMIENTO DE FECHA ######################
#def DectivandoSocios(request):
#	hoy = datetime.today().date()
#	socios = tb_socio.objects.all()
#	for i in range(0,len(socios)):
#		if(socios[i].dateInactive_socio == hoy):
#			socios[i].status = 'Desactivado'
#			socios[i].save()
			###ENVIAR EL CORREO QUE SE DESACTIVO EL PERFIL ########
#			VencimientoMensualidad.delay(socios[i].perfil.nameUser, socios[i].TarifaMensual.precioPlan, socios[i].TarifaMensual.nombrePlan, socios[i].perfil.mailUser)
#	return HttpResponse(200)




#######################LISTA DE SOCIOS ##############################
@login_required(login_url = 'Panel:Login' )
def ListaDeSocios(request):
	socios = tb_socio.objects.all()
	contexto = {
	'socios':socios
	}
	return render (request, 'Socios/ListadoDeSocios.html', contexto)



##########################NUEVO SOCIO################################

def NewSocio(request):
	#print('esto esta por funcionar')
	Form = UsuarioForm()
	Form2 = ProfileForm()
	Form3 = SociosRegisterForm()
	planes =  tb_plan.objects.all()
	planes_diarios = tb_plan_diario.objects.all()
	descuentos = tb_porcentaje.objects.all()
	fallido = None
	if request.method == 'POST':
		print(request.POST)
		#Form  = UsuarioForm(request.POST, request.FILES  or None)
		Form2 = ProfileForm(request.POST, request.FILES  or None)
		Form3 = SociosRegisterForm(request.POST, request.FILES  or None)
		if Form2.is_valid() and Form3.is_valid():
			print('validos')
			nuevoPerfil = Form2.save(commit=False)
			#nuevoPerfil.user = 
			nuevoPerfil.nameUser = request.POST['nameUser']
			nuevoPerfil.dni = request.POST['dni']
			nuevoPerfil.mailUser = request.POST['mailUser']
			nuevoPerfil.tipoUser = 'Socio'
			if len(request.FILES) != 0:
				nuevoPerfil.image = request.FILES['ImagenDePerfil']
			else:
				nuevoPerfil.image = 'Null'
			nuevoPerfil.save()
			print('paso1')
			nuevoSocio = Form3.save(commit=False)
			nuevoSocio.perfil = tb_profile.objects.get(id = nuevoPerfil.id)
			nuevoSocio.obraSocial =  request.POST['obraSocial']
			nuevoSocio.status = 'Activo'
			print('paso2')
			if( float(request.POST['IdPlanSeleccionado']) > 0):
				nuevoSocio.TarifaMensual = tb_plan.objects.get(id = request.POST['IdPlanSeleccionado'])
				nuevoSocio.dateInactive_socio = request.POST['dateInactive_socio']
				nuevoSocio.IsMensualAnual = True
				nuevoSocio.IsDiario = False
				if( float(request.POST['IdDescuentoSeleccionado']) > 0):
					division = float(request.POST['IdDescuentoSeleccionado']) / 100
					multiplicacion = float(nuevoSocio.TarifaMensual.precioPlan) * division
					total = float(nuevoSocio.TarifaMensual.precioPlan) - multiplicacion
					nuevoSocio.TarifaconDescuento = total
					print(nuevoSocio.TarifaconDescuento)
					nuevoSocio.descuento = True
				else: 
					nuevoSocio.TarifaconDescuento = 0
					print(nuevoSocio.TarifaconDescuento)
					nuevoSocio.descuento = False
				nuevoSocio.save()
				print('guardémensual')
			#NewSocioMAil.delay(request.POST['nameUser'], nuevoSocio.TarifaMensual.precioPlan, nuevoSocio.TarifaMensual.nombrePlan, request.POST['mailUser'])
			else:
				nuevoSocio.IsMensualAnual = False
				nuevoSocio.IsDiario = True
				nuevoSocio.TarifaDiaria = tb_plan_diario.objects.get(id = request.POST['IdPlanDiarioSeleccionado'])
				nuevoSocio.dateInactive_socio = request.POST['dateInactive_socio']
				nuevoSocio.save()
				print('guardédiario')
			return redirect('Socios:ListaDeSocios')
		else:
			#Form	= UsuarioForm(request.POST , request.FILES  or None)
			Form2	= ProfileForm(request.POST, request.FILES  or None)
			Form3 = SociosRegisterForm(request.POST, request.FILES  or None)
			fallido = "No pudimos guardar sus datos, intentalo de nuevo luego de verificarlos" 
	contexto = {
	#'Form':Form,
	'Form2':Form2,
	'Form3':Form3,
	'planes':planes,
	'planes_diarios':planes_diarios,
	'descuentos':descuentos,
	'fallido':fallido,
	}
	return render(request, 'Socios/NuevoSocio.html' , contexto)






def UpdateSocio(request, id_socio):
	socio= tb_socio.objects.get(id=id_socio)
	perfil = tb_profile.objects.get(id = socio.perfil.id)
	planes =  tb_plan.objects.all()
	planes_diarios = tb_plan_diario.objects.all()
	descuentos = tb_porcentaje.objects.all()
	fallido = None
	if request.method == 'GET':
		Form2= ProfileForm(instance = perfil)
		Form3 = SociosRegisterForm(instance = socio)
	else:
		Form2 = ProfileForm(request.POST , request.FILES  ,  instance = perfil)
		Form3 = SociosRegisterForm(request.POST , request.FILES  ,  instance = socio)
		if Form2.is_valid() and Form3.is_valid():
			nuevoPerfil = Form2.save(commit=False)
			#nuevoPerfil.user = 
			nuevoPerfil.nameUser = request.POST['nameUser']
			nuevoPerfil.dni = request.POST['dni']
			nuevoPerfil.mailUser = request.POST['mailUser']
			nuevoPerfil.tipoUser = 'Socio'
			if len(request.FILES) != 0:
				nuevoPerfil.image = request.FILES['ImagenDePerfil']
			else:
				nuevoPerfil.image = 'Null'
			nuevoPerfil.save()
			nuevoSocio = Form3.save(commit=False)
			nuevoSocio.perfil = tb_profile.objects.get(id = nuevoPerfil.id)
			nuevoSocio.obraSocial =  request.POST['obraSocial']
			nuevoSocio.status = 'Activo'
			print('paso2')
			if( float(request.POST['IdPlanSeleccionado']) > 0):
				nuevoSocio.TarifaMensual = tb_plan.objects.get(id = request.POST['IdPlanSeleccionado'])
				nuevoSocio.dateInactive_socio = request.POST['dateInactive_socio']
				nuevoSocio.IsMensualAnual = True
				nuevoSocio.IsDiario = False
				if( float(request.POST['IdDescuentoSeleccionado']) > 0):
					division = float(request.POST['IdDescuentoSeleccionado']) / 100
					multiplicacion = float(nuevoSocio.TarifaMensual.precioPlan) * division
					total = float(nuevoSocio.TarifaMensual.precioPlan) - multiplicacion
					nuevoSocio.TarifaconDescuento = total
					print(nuevoSocio.TarifaconDescuento)
					nuevoSocio.descuento = True
				else: 
					nuevoSocio.TarifaconDescuento = 0
					print(nuevoSocio.TarifaconDescuento)
					nuevoSocio.descuento = False
				nuevoSocio.save()
				print('guardémensual')
			#NewSocioMAil.delay(request.POST['nameUser'], nuevoSocio.TarifaMensual.precioPlan, nuevoSocio.TarifaMensual.nombrePlan, request.POST['mailUser'])
			else:
				nuevoSocio.IsMensualAnual = False
				nuevoSocio.IsDiario = True
				nuevoSocio.TarifaDiaria = tb_plan_diario.objects.get(id = request.POST['IdPlanDiarioSeleccionado'])
				nuevoSocio.dateInactive_socio = request.POST['dateInactive_socio']
				nuevoSocio.save()
				print('guardédiario')
			return redirect('Socios:ListaDeSocios')
		else:
			#Form	= UsuarioForm(request.POST , request.FILES  or None)
			Form2	= ProfileForm(request.POST, request.FILES  or None)
			Form3 = SociosRegisterForm(request.POST, request.FILES  or None)
			fallido = "No pudimos guardar sus datos, intentalo de nuevo luego de verificarlos" 
	return render (request, 'Socios/NuevoSocio.html' , {'Form2':Form2,'Form3':Form3,'planes':planes,'planes_diarios':planes_diarios,'descuentos':descuentos,'fallido':fallido,})

#########################ELIMINAR SOCIO ##############################

def DeleteSocio(request):
	status 		= None
	id_socio 	= 	request.GET.get('id_socio', None)
	socio  	=	tb_socio.objects.get(id = id_socio)
	print (id_socio)
	socio.delete()
	status 		=	200
	return HttpResponse(status)

#########################DESACTIVAR SOCIO#############################

def DesactivateSocio(request):
	id_socio = request.GET.get('id', None)
	queryset = tb_socio.objects.get(id = id_socio)
	queryset.status = 'Desactivado'
	queryset.IsDiario = False
	queryset.isPay = False
	# DesactivacionSocio.delay(queryset.perfil.nameUser, queryset.TarifaMensual.precioPlan, queryset.TarifaMensual.nombrePlan, queryset.perfil.mailUser)
	queryset.save()
	return HttpResponse(200)

#########################DESACTIVAR SOCIO#############################
def ActivateSocio(request):
	id_socio = request.GET.get('id', None)
	queryset = tb_socio.objects.get(id = id_socio)
	queryset.status = 'Activo'
	queryset.save()
	ActivacionSocio.delay(queryset.perfil.nameUser,  queryset.perfil.mailUser)
	return HttpResponse(200)





def ActivacionSocioMensualAnual(request):
	status = None
	id_socio = request.GET.get('id_socio', None)
	anual_mensual = request.GET.get('mensual_anual', None)
	forma_pago = request.GET.get('forma_pago', None)
	#activar socio, anual, mensual 
	socio = tb_socio.objects.get(id = id_socio)
	if anual_mensual == 'Mensual':
		#activo al socio mensual
		socio.status = 'Activo'
		socio.isPay = True
		socio.dateInactive_socio = Desactivate_Register(socio.dateInactive_socio, 1)
		socio.save()
	elif anual_mensual == "Anual":
		#activo al socio por todo el a#o 
		socio.status = 'Activo'
		socio.isPay = True
		socio.dateInactive_socio = Desactivate_Register(socio.dateInactive_socio, 12)
		socio.save()
	if socio.descuento == False:	
		ingreso = tb_ingreso_mensualidad()
		#GENRAR INGRESO 
		ingreso.user = request.user
		ingreso.plan = tb_plan.objects.get(nombrePlan = socio.TarifaMensual)
		if anual_mensual == 'Mensual':
			ingreso.monto = socio.TarifaMensual.precioPlan
		elif anual_mensual == "Anual":
			ingreso.monto = socio.TarifaMensual.precioPlanAnual
		ingreso.descripcion = 'Pago. Abono Mensual del Asociado.'
		ingreso.tipoPago = tb_formasDePago.objects.get(nameFormasDePago = forma_pago )
		ingreso.nombre = socio.perfil.nameUser
		ingreso.apellido = socio.perfil.lastName
		ingreso.correo  = socio.perfil.mailUser
		ingreso.save()
		status = 200
		return HttpResponse(status)
	elif socio.descuento == True:
		ingreso = tb_ingreso_mensualidad()
		#GENRAR INGRESO 
		ingreso.user = request.user
		ingreso.plan = tb_plan.objects.get(nombrePlan = socio.TarifaMensual)
		if anual_mensual == 'Mensual':
			ingreso.monto = socio.TarifaconDescuento
		elif anual_mensual == "Anual":
			ingreso.monto = socio.TarifaMensual.precioPlanAnual
		ingreso.descripcion = 'Pago. Abono Mensual del Asociado con descuento.'
		ingreso.tipoPago = tb_formasDePago.objects.get(nameFormasDePago = forma_pago )
		ingreso.nombre = socio.perfil.nameUser
		ingreso.apellido = socio.perfil.lastName
		ingreso.correo  = socio.perfil.mailUser
		ingreso.save()
		status = 200
		return HttpResponse(status)




def NuevoReporteDePagoParcialMensual(request):
	status = 200
	id_socio = request.GET.get('id_socio', None)
	
	id_monto  = float (request.GET.get('id_monto', None))
	
	forma_pago = request.GET.get('forma_pago', None)
	
	socio = tb_socio.objects.get(id = id_socio)
	precioPlan = float(socio.TarifaMensual.precioPlan)
	precioPlandescuento = float(socio.TarifaconDescuento)
	socio.montoPagado += id_monto
	socio.save()
	if socio.descuento == False:
		
		if precioPlan != socio.montoPagado or socio.montoPagado == 0 and id_monto != precioPlan:
			socio.isPay = False
			socio.status = 'Activo'
		elif socio.montoPagado == precioPlan:
			socio.isPay = True
			socio.status = 'Activo'
			socio.save()
	elif socio.descuento == True:
		if precioPlandescuento != socio.montoPagado or socio.montoPagado == 0 and id_monto != precioPlandescuento:
			socio.isPay = False
			socio.status = 'Activo'
		elif socio.montoPagado == precioPlandescuento:
			socio.isPay = True
			socio.status = 'Activo'
			socio.save()
	print(socio.descuento)
	print (type (precioPlan))
	ingreso = tb_ingreso_mensualidad()
	ingreso.user = request.user
	ingreso.plan = tb_plan.objects.get(nombrePlan = socio.TarifaMensual)
	ingreso.tipoPago = tb_formasDePago.objects.get(nameFormasDePago = forma_pago )
	ingreso.monto = id_monto
	ingreso.descripcion = 'Pago Parcial de Mensualidad'
	ingreso.nombre = socio.perfil.nameUser
	ingreso.apellido = socio.perfil.lastName
	ingreso.correo  = socio.perfil.mailUser
	ingreso.save()
	status = 200
		
	return HttpResponse(status)


def Descuento(request):
	status = 200
	id_socio = request.GET.get('id_socio', None)
	porcentajesop  = float (request.GET.get('porcentajesop', None))
	porcentajeapli = porcentajesop / 100
	socio = tb_socio.objects.get(id = id_socio)
	precioPlan = float(socio.TarifaMensual.precioPlan) 
	porcentajeTotal = precioPlan * porcentajeapli 
	Totalplan = precioPlan - porcentajeTotal
	socio.TarifaconDescuento = Totalplan
	socio.descuento = True 
	print(Totalplan)
	socio.save()
	status = 200
		
	return HttpResponse(status)

def UpdatePlan(request, id_socio):
	socio= tb_socio.objects.get(id=id_socio)
	planes =  tb_plan.objects.all()
	planes_diarios = tb_plan_diario.objects.all()
	descuentos = tb_porcentaje.objects.all()
	fallido = None
	if request.method == 'GET':
		Form3 = PlanUpdateForm(instance = socio)
	else:
		Form3 = PlanUpdateForm(request.POST , request.FILES  ,  instance = socio)
		if Form3.is_valid():
			nuevoSocio = Form3.save(commit=False)
			nuevoSocio.obraSocial =  request.POST['obraSocial']
			nuevoSocio.status = 'Activo'
			print('paso2')
			if( float(request.POST['IdPlanSeleccionado']) > 0):
				nuevoSocio.TarifaMensual = tb_plan.objects.get(id = request.POST['IdPlanSeleccionado'])
				nuevoSocio.dateInactive_socio = request.POST['dateInactive_socio']
				nuevoSocio.IsMensualAnual = True
				nuevoSocio.IsDiario = False
				if( float(request.POST['IdDescuentoSeleccionado']) > 0):
					division = float(request.POST['IdDescuentoSeleccionado']) / 100
					multiplicacion = float(nuevoSocio.TarifaMensual.precioPlan) * division
					total = float(nuevoSocio.TarifaMensual.precioPlan) - multiplicacion
					nuevoSocio.TarifaconDescuento = total
					print(nuevoSocio.TarifaconDescuento)
					nuevoSocio.descuento = True
				else: 
					nuevoSocio.TarifaconDescuento = 0
					print(nuevoSocio.TarifaconDescuento)
					nuevoSocio.descuento = False
				nuevoSocio.save()
				print('guardémensual')
			#NewSocioMAil.delay(request.POST['nameUser'], nuevoSocio.TarifaMensual.precioPlan, nuevoSocio.TarifaMensual.nombrePlan, request.POST['mailUser'])
			else:
				nuevoSocio.IsMensualAnual = False
				nuevoSocio.IsDiario = True
				nuevoSocio.TarifaDiaria = tb_plan_diario.objects.get(id = request.POST['IdPlanDiarioSeleccionado'])
				nuevoSocio.dateInactive_socio = request.POST['dateInactive_socio']
				nuevoSocio.save()
				print('guardédiario')
			return redirect('Socios:ListaDeSocios')
		else:
			
			Form3 = PlanUpdateForm(request.POST, request.FILES  or None)
			fallido = "No pudimos guardar sus datos, intentalo de nuevo luego de verificarlos" 
	return render (request, 'Socios/UpdatePlan.html' , {'Form3':Form3,'planes':planes,'planes_diarios':planes_diarios,'descuentos':descuentos,'fallido':fallido,})


def NuevoReporteDePagoDiario(request):
	status = 200
	id_socio = request.GET.get('id_socio', None)
	id_monto  = float (request.GET.get('id_monto', None))
	forma_pago = request.GET.get('forma_pago', None)
	socio = tb_socio.objects.get(id = id_socio)
	precioPlan = float(socio.TarifaDiaria.precioPlan)
	socio.montoPagado += id_monto
	socio.save()
	if precioPlan != socio.montoPagado or socio.montoPagado == 0 and id_monto != precioPlan:
		socio.isPay = False
		socio.status = 'Activo'
	elif socio.montoPagado == precioPlan:
		socio.isPay = True
		socio.status = 'Activo'
		socio.save()
	print (type (precioPlan))
	ingreso = tb_ingresos()
	ingreso.user = request.user
	ingreso.plan = tb_plan_diario.objects.get(nombrePlan = socio.TarifaDiaria)
	ingreso.tipoPago = tb_formasDePago.objects.get(nameFormasDePago = forma_pago )
	ingreso.monto = id_monto
	ingreso.descripcion = 'Pago Parcial de Mensualidad'
	ingreso.save()
	status = 200
	return HttpResponse(status)

def ActivacionSocioDiario(request):
	status = None
	id_socio = request.GET.get('id_socio', None)
	si_no = request.GET.get('si_no', None)
	forma_pago = request.GET.get('forma_pago', None)
	#activar socio, anual, mensual 
	socio = tb_socio.objects.get(id = id_socio)
	#activo al socio mensual
	socio.status = 'Activo'
	socio.isPay = True
	socio.dateInactive_socio = Desactivate_Register(socio.dateInactive_socio, 1)
	socio.save()
	ingreso = tb_ingresos()
	ingreso.user = request.user
	ingreso.plan = tb_plan_diario.objects.get(nombrePlan = socio.TarifaDiaria)
	ingreso.tipoPago = tb_formasDePago.objects.get(nameFormasDePago = forma_pago )
	ingreso.monto = socio.TarifaDiaria.precioPlan
	ingreso.tipoDeIngresos = tb_tipoIngreso.objects.get(id = 1)
	ingreso.descripcion = 'Pago Plan Diario'
	ingreso.save()
	status = 200
	return HttpResponse(status)