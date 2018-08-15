from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from apps.UserProfile.models import tb_profile
from apps.ContextProcesor.UserProfile import QueryUser
from apps.tasks.Process_tasks import ActualizacionDeUsuarios
from django.http import HttpResponse
# Create your views here.




def ActualizacionUsuario(request):
	ActualizacionDeUsuarios.delay()
	return HttpResponse(200)



def ComingSoon(request):
	return render(request, 'Panel/ComingSoon.html')



@login_required(login_url = 'Panel:Login' )
def Inicio(request):
	if QueryUser(request.user.id) == False:
		return redirect('Usuarios:Perfil')
	return render(request, 'Panel/Inicio.html')

def Login(request):
	logout_django(request)
	mensaje = None
	if request.method=="POST":
		user = request.POST['username']
		passw	=	request.POST['password']
		usuario = authenticate(username=user , password = passw)
		if usuario is not None:
			login_django(request, usuario)
			query_perfil = tb_profile.objects.filter(user__id = request.user.id)
			if len(query_perfil) != 0:
				perfil_usuario = query_perfil[0]
			else:
				perfil_usuario = None
			if QueryUser(request.user.id) == False or perfil_usuario.is_complete == False :
				#No tiene Perfil
				return redirect('Usuarios:Perfil')
			else:
				#tiene perfil
				return redirect('/')
		else:
			mensaje = "Usuario o password incorrectas"
	return render (request, 'Panel/Login.html', {'mensaje':mensaje})

def Logout(request):
	logout_django(request)
	return redirect('Panel:Login')