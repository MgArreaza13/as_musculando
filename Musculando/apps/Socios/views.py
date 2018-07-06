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
from django.contrib.auth.models import User ##MODULE LO USUARIO DE DJANGO
from apps.Caja.models import tb_ingreso_mensualidad
from apps.UserProfile.models import tb_profile
#######FORMULARIOS#############
from apps.UserProfile.forms import UsuarioForm
from apps.UserProfile.forms import ProfileForm
from apps.Socios.forms import SociosRegisterForm


##########SCRIPTS################
from apps.Scripts.DesactivateUser import Desactivate_Register


######################CELERY################
from apps.tasks.Email_tasks import VencimientoMensualidad
from apps.tasks.Email_tasks import NewSocioMAil
from apps.tasks.Email_tasks import DesactivacionSocio
from apps.tasks.Email_tasks import ActivacionSocio
from apps.tasks.Email_tasks import PerfilEliminado
from apps.tasks.Email_tasks import GetProfile





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
	fallido = None
	if request.method == 'POST':
		#Form  = UsuarioForm(request.POST, request.FILES  or None)
		Form2 = ProfileForm(request.POST, request.FILES  or None)
		Form3 = SociosRegisterForm(request.POST, request.FILES  or None)
		if Form2.is_valid() and Form3.is_valid():
			#print('validos')
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
			nuevoSocio.TarifaMensual = tb_plan.objects.get(id = request.POST['IdPlanSeleccionado'])
			nuevoSocio.dateInactive_socio = request.POST['dateInactive_socio']
			nuevoSocio.save() 
				################ENVIAR CORREO QUE SE CREO EL PERFIL DE SOCIO CORRECTAMENTE ########
			NewSocioMAil.delay(request.POST['nameUser'], nuevoSocio.TarifaMensual.precioPlan, nuevoSocio.TarifaMensual.nombrePlan, request.POST['mailUser'])
			#print('miguel')
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
	'fallido':fallido,
	}
	return render(request, 'Socios/NuevoSocio.html' , contexto)






def UpdateSocio(request, id_socio):
	socio= tb_socio.objects.get(id=id_socio)
	perfil = tb_profile.objects.get(id = socio.perfil.id)
	planes =  tb_plan.objects.all()
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
			nuevoSocio.obraSocial =  request.POST['obraSocial']
			nuevoSocio.status = 'Activo'
			nuevoSocio.TarifaMensual = tb_plan.objects.get(id = request.POST['IdPlanSeleccionado'])
			nuevoSocio.dateInactive_socio = request.POST['dateInactive_socio']
			nuevoSocio.save() 
				################ENVIAR CORREO QUE SE CREO EL PERFIL DE SOCIO CORRECTAMENTE ########
			#NewSocioMAil.delay(request.POST['nameUser'], nuevoSocio.TarifaMensual.precioPlan, nuevoSocio.TarifaMensual.nombrePlan, request.POST['mailUser'])
			return redirect('Socios:ListaDeSocios')
		else:
			#Form	= UsuarioForm(request.POST , request.FILES  or None)
			Form2	= ProfileForm(request.POST, request.FILES  or None)
			Form3 = SociosRegisterForm(request.POST, request.FILES  or None)
			fallido = "No pudimos guardar sus datos, intentalo de nuevo luego de verificarlos" 
	return render (request, 'Socios/NuevoSocio.html' , {'Form2':Form2,'Form3':Form3,'planes':planes,'fallido':fallido,})

#########################ELIMINAR SOCIO ##############################

def DeleteSocio(request):
	status = None
	id_usuario = request.GET.get('id', None)
	queryset = User.objects.get(id = id_usuario)
	PerfilEliminado.delay()
	queryset.delete()
	status = 200
	return HttpResponse(status)



#########################DESACTIVAR SOCIO#############################

def DesactivateSocio(request):
	id_socio = request.GET.get('id', None)
	queryset = tb_socio.objects.get(id = id_socio)
	queryset.status = 'Desactivado'
	DesactivacionSocio.delay(queryset.perfil.nameUser, queryset.TarifaMensual.precioPlan, queryset.TarifaMensual.nombrePlan, queryset.perfil.mailUser)
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
	forma_de_pago = request.GET.get('forma_pago', None)
	#activar socio, anual, mensual 
	socio = tb_socio.objects.get(id = id_socio)
	if anual_mensual == 'Mensual':
		#activo al socio mensual
		socio.status = 'Activo'
		socio.dateInactive_socio = Desactivate_Register(socio.dateInactive_socio, 1)
		socio.save()
	elif anual_mensual == "Anual":
		#activo al socio por todo el a#o 
		socio.status = 'Activo'
		socio.dateInactive_socio = Desactivate_Register(socio.dateInactive_socio, 12)
		socio.save()
	ingreso = tb_ingreso_mensualidad()
	#GENRAR INGRESO 
	ingreso.user = request.user
	ingreso.plan = tb_plan.objects.get(nombrePlan = socio.TarifaMensual)
	if anual_mensual == 'Mensual':
		ingreso.monto = socio.TarifaMensual.precioPlan
	elif anual_mensual == "Anual":
		ingreso.monto = socio.TarifaMensual.precioPlanAnual
	ingreso.descripcion = 'Pago. Abono Mensual del Asociado.'
	ingreso.nombre = socio.perfil.nameUser
	ingreso.apellido = socio.perfil.lastName
	ingreso.correo  = socio.perfil.mailUser
	ingreso.save()
	status = 200
	return HttpResponse(status)




