from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
########## MODELOS ###############
from apps.UserProfile.models import tb_profile
##########FORMULARIOS##############
from apps.UserProfile.forms import ProfileRegisterForm
from apps.UserProfile.forms import ProfileForm
from apps.UserProfile.forms import UsuarioForm
from apps.ContextProcesor.UserProfile import QueryUser
# Create your views here.


#Registro debug
@login_required(login_url = 'Panel:Login' )
def RegisterDebug(request):
	Form = UsuarioForm()
	if request.method == 'POST':
		Form = UsuarioForm(request.POST, request.FILES  or None)
		if Form.is_valid():
			Form.save()
			return redirect('Usuarios:Perfil')
	return render(request, 'UserProfile/NuevoUsuario.html', {'Form':Form})


#registro de usuario sistema
@login_required(login_url = 'Panel:Login' )
def RegistroUser(request):
	Form = UsuarioForm()
	Form2 = ProfileRegisterForm()
	fallido = None
	if request.method == 'POST':
		Form  = UsuarioForm(request.POST, request.FILES  or None)
		Form2 = ProfileRegisterForm(request.POST, request.FILES  or None)
		if Form.is_valid() and Form2.is_valid():
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
				nuevoPerfil.tipoUser = request.POST['tipoUser']
				nuevoPerfil.save()
				return redirect('Usuarios:Perfil')
			else:
				Form	= UsuarioForm(request.POST , request.FILES  or None)
				Form2	= ProfileRegisterForm(request.POST, request.FILES  or None)
				fallido = "No pudimos guardar sus datos, intentalo de nuevo luego de verificarlos" 
	contexto = {
	'Form':Form,
	'Form2':Form2,
	'fallido':fallido,
	}
	return render(request, 'UserProfile/NuevoUsuario.html' , contexto)




#Acrualizacion y nuevo perfil a la vez 
@login_required(login_url = 'Panel:Login' )
def Perfil(request):
	perfil = tb_profile.objects.filter(user__id = request.user.id)
	is_perfil = None
	if QueryUser(request.user.id) == False or perfil[0].is_complete == False :
		#No tiene Perfil
		is_perfil = False
	else:
		#tiene perfil
		is_perfil = True
	if len(perfil) == 0:
		Form = ProfileForm()
	else:
		Form= ProfileForm(instance=perfil[0])
	if request.method == 'POST':
		if len(perfil)== 0:
			Form  = ProfileForm(request.POST, request.FILES  or None)
		else:
			UserProfile = perfil[0]
			Form  = ProfileForm(request.POST, 
				request.FILES , instance=UserProfile)
		if Form.is_valid():
			perfil = Form.save(commit=False)
			perfil.user = request.user
			if len(request.FILES) != 0:
				perfil.image = request.FILES['ImagenDePerfil']
			else:
				perfil.image = 'Null'
			perfil.is_complete = True
			perfil.save()
			return redirect('Usuarios:Perfil')
	contexto = {
	'Form':Form,
	'is_perfil':is_perfil,
	}
	return render(request, 'UserProfile/Profile.html', contexto )


@login_required(login_url = 'Panel:Login' )
def ListadoDeUsuarios(request):
	usuarios = tb_profile.objects.all()
	contexto = {
	'usuarios':usuarios,
	}
	return render(request, 'UserProfile/List.html', contexto)