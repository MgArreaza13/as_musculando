from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
###############MODELOS################
from apps.Configuracion.models import tb_plan


##############FORMULARIOS################
from apps.Configuracion.forms import PlanRegisterForm

# Create your views here.



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
		new_plan.save()
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
	descripcion = request.GET.get('Descripcion', None)
	queryset =  tb_plan.objects.filter(nombrePlan = titulo)
	if(len(queryset)>=1):
		status = 400
	else:
		queryset =  tb_plan.objects.get(id = id_plan)
		queryset.nombrePlan = titulo
		queryset.precioPlan = precio 
		queryset.descripcionPlan = descripcion
		queryset.save()
		status = 200
	return HttpResponse(status)