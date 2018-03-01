from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

###############MODELOS#############
from apps.Clases.models import tb_clase

# Create your views here.

@login_required(login_url = 'Panel:Login' )
def ListadoDeClases(request):
	listaDeClases = tb_clase.objects.all()
	contexto = {
	'listaDeClases':listaDeClases,
	}
	return render(request, 'Clases/ListaDeClases.html', contexto)