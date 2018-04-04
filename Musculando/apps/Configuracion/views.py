from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
###############MODELOS################
from apps.Configuracion.models import tb_plan
from apps.Configuracion.models import tb_formasDePago
from apps.Socios.models import tb_socio

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



################################CONFIGURACION GENERAL###############################
def Configuracion_g(request):
	formas_de_pago = tb_formasDePago.objects.all()
	contexto = {
	'formas_de_pago':formas_de_pago,
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