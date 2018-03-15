from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import datetime
########Modelos################
from apps.Socios.models import tb_socio
from apps.Configuracion.models import tb_plan
from django.contrib.auth.models import User ##MODULE LO USUARIO DE DJANGO
#######FORMULARIOS#############
from apps.UserProfile.forms import UsuarioForm
from apps.UserProfile.forms import ProfileForm
from apps.Socios.forms import SociosRegisterForm
from apps.UserProfile.models import tb_profile

##########SCRIPTS################

from apps.Scripts.DesactivateUser import Desactivate_Register

# Create your views here.






#####################FUNCION QUE DESACTIVA SOCIOS######################
def DectivandoSocios(request):
	hoy = datetime.today().date()
	socios = tb_socio.objects.all()
	for i in range(0,len(socios)):
		if(socios[i].dateInactive_socio == hoy):
			socios[i].status = 'Desactivado'
			socios[i].save()
	return HttpResponse(200)




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
	Form = UsuarioForm()
	Form2 = ProfileForm()
	Form3 = SociosRegisterForm()
	planes =  tb_plan.objects.all()
	fallido = None
	if request.method == 'POST':
		Form  = UsuarioForm(request.POST, request.FILES  or None)
		Form2 = ProfileForm(request.POST, request.FILES  or None)
		Form3 = SociosRegisterForm(request.POST, request.FILES  or None)
		if Form.is_valid():
			Form.save()
			usuario = request.POST['username']
			clave 	= request.POST['password1']
			user 	= authenticate(username=usuario, password=clave)
			if user is not None and user.is_active:
				nuevoPerfil = tb_profile()
				nuevoPerfil.user = user
				nuevoPerfil.nameUser = request.POST['nameUser']
				nuevoPerfil.dni = request.POST['dni']
				nuevoPerfil.mailUser = request.POST['mailUser']
				nuevoPerfil.tipoUser = 'Socio'
				if len(request.FILES) != 0:
					nuevoPerfil.image = request.FILES['ImagenDePerfil']
				else:
					nuevoPerfil.image = 'Null'
				nuevoPerfil.save()
				nuevoSocio = tb_socio()
				nuevoSocio.perfil = tb_profile.objects.get(id = nuevoPerfil.id)
				nuevoSocio.obraSocial =  request.POST['obraSocial']
				nuevoSocio.status = 'Activo'
				nuevoSocio.TarifaMensual = tb_plan.objects.get(id = request.POST['IdPlanSeleccionado'])
				nuevoSocio.dateInactive_socio = Desactivate_Register(datetime.today().date() , 1)
				nuevoSocio.save() 
				return redirect('Socios:ListaDeSocios')
			else:
				Form	= UsuarioForm(request.POST , request.FILES  or None)
				Form2	= ProfileForm(request.POST, request.FILES  or None)
				Form3 = SociosRegisterForm(request.POST, request.FILES  or None)
				fallido = "No pudimos guardar sus datos, intentalo de nuevo luego de verificarlos" 
	contexto = {
	'Form':Form,
	'Form2':Form2,
	'Form3':Form3,
	'planes':planes,
	'fallido':fallido,
	}
	return render(request, 'Socios/NuevoSocio.html' , contexto)

#########################ELIMINAR SOCIO ##############################

def DeleteSocio(request):
	queryset_user = User.objects.all()
	status = None
	id_usuario = request.GET.get('id', None)
	queryset = User.objects.get(id = id_usuario)
	queryset.delete()
	status = 200
	return HttpResponse(status)



#########################DESACTIVAR SOCIO#############################

def DesactivateSocio(request):
	id_socio = request.GET.get('id', None)
	queryset = tb_socio.objects.get(id = id_socio)
	queryset.status = 'Desactivado'
	queryset.save()
	return HttpResponse(200)

#########################DESACTIVAR SOCIO#############################
def ActivateSocio(request):
	id_socio = request.GET.get('id', None)
	queryset = tb_socio.objects.get(id = id_socio)
	queryset.status = 'Activo'
	queryset.save()
	return HttpResponse(200)
