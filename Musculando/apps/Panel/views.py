from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django

# Create your views here.

@login_required(login_url = 'Panel:Login' )
def Inicio(request):
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
			return redirect('/')
		else:
			mensaje = "Usuario o password incorrectas"
	return render (request, 'Panel/Login.html', {'mensaje':mensaje})

def Logout(request):
	logout_django(request)
	return redirect('Panel:Login')