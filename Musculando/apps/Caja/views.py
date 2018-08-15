from django.shortcuts import render
from django.contrib.auth.models import User 
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core import serializers
#################MODELOS###################
from apps.Socios.models import tb_socio
from apps.Caja.models import tb_egreso
from apps.Caja.models import tb_ingreso_mensualidad
from apps.Colaboradores.models import tb_colaboradores
from apps.Configuracion.models import tb_plan
from apps.Configuracion.models import tb_tipoEgreso
from apps.Proveedores.models import tb_proveedor
from django.contrib.auth.decorators import login_required
from apps.Configuracion.models import tb_tipoIngreso
from apps.Caja.models import tb_ingresos
##################FORMULARIOS#############################
from apps.Caja.forms import EgresoRegisterForm
from apps.Caja.forms import IngresoRegisterForm

################SCRIPTS#########################
from apps.Scripts.DesactivateUser import Desactivate_Register
# Create your views here.
#################tareas asincronas correos ##########################
from apps.tasks.Email_tasks import MailNewIngresoMensualidad
from django.db.models import Count, Min, Sum, Avg
from apps.Caja.models import tb_cierre_de_caja
from datetime import date
import time
import json



def VerCierre(request, id_cierre):
	cierre = tb_cierre_de_caja.objects.get(id = id_cierre)
	ingresos_today = json.loads(cierre.ingresos)
	ingresos_mensualidades = json.loads(cierre.ingresos_mensualidades)
	egresos = json.loads(cierre.egresos)

	ingresos = []
	egresos_d = []

	for i in range(0,len(ingresos_today)):
		
		ingresos.append({'ingresos':'Mensualidades', 'descripcion':ingresos_today[i]['fields']['descripcion'], 'fecha':ingresos_today[i]['fields']['dateCreate'], 'monto':ingresos_today[i]['fields']['monto']})
	for i in range(0,len(ingresos_mensualidades)):
	
		ingresos.append({'ingresos':tb_tipoIngreso.objects.get(id = ingresos_mensualidades[i]['fields']['tipoDeIngresos'] ), 'descripcion':ingresos_mensualidades[i]['fields']['descripcion'], 'fecha':ingresos_mensualidades[i]['fields']['dateCreate'], 'monto':ingresos_mensualidades[i]['fields']['monto']})
	for i in range(0,len(egresos)):
		
		egresos_d.append({'egresos':tb_tipoEgreso.objects.get(id = egresos[i]['fields']['tipoDeEgreso']), 'descripcion':egresos[i]['fields']['descripcion'], 'fecha':egresos[i]['fields']['dateCreate'], 'monto':egresos[i]['fields']['monto']})

	
	
	contexto = {
		'cierre':cierre,
		'ingresos':ingresos,
		'egresos_d':egresos_d,
		'egresos':egresos,
	}
	return render(request, 'Caja/Cierre_detail.html', contexto )





@login_required(login_url = 'Panel:Login' )
def ResumenCierres(request):
	cierres = tb_cierre_de_caja.objects.all()
	contexto = {
		'cierres':cierres
	}
	return render(request , 'Caja/ResumenCierre.html', contexto )



@login_required(login_url = 'Panel:Login' )
def Cierre(request):
	hoy = date.today()
	hora = time.strftime("%H:%M:%S")
	cierre = tb_cierre_de_caja()
	ingresos_today =  tb_ingreso_mensualidad.objects.filter(dateCreate = hoy)
	mensualidades_today = tb_ingresos.objects.filter(dateCreate = hoy)
	egresos = tb_egreso.objects.filter(dateCreate = hoy)
	total_ingresos_today = tb_ingreso_mensualidad.objects.filter(dateCreate = hoy).aggregate(total=Sum('monto'))
	total_mensualidades_today = tb_ingresos.objects.filter(dateCreate = hoy).aggregate(total=Sum('monto'))
	total_egresos= tb_egreso.objects.filter(dateCreate = hoy).aggregate(total=Sum('monto'))
	if total_ingresos_today['total'] == None:
		total_ingresos_today['total'] = 0
	if total_mensualidades_today['total'] == None:
		total_mensualidades_today['total'] = 0
	if total_egresos['total'] == None:
		total_egresos['total'] = 0
	total_ingresos = total_ingresos_today['total'] + total_mensualidades_today['total']
	balance_general = total_ingresos - total_egresos['total']
	cierre.user = request.user
	cierre.hora = time.strftime("%H:%M:%S")
	cierre.ingresos_mensualidades = serializers.serialize("json", ingresos_today)
	cierre.ingresos = serializers.serialize("json", mensualidades_today)
	cierre.egresos = serializers.serialize("json", egresos)
	cierre.totalIngresos = float(total_ingresos)
	cierre.totalEgresos = float(total_egresos['total'])
	cierre.balanceGeneral = float(balance_general)
	cierre.save()


	
	 
	
	context = {
		'total_ingresos':total_ingresos,
		'balance_general':balance_general,
		'total_egresos':total_egresos,
		'ingresos_today':ingresos_today,
		'mensualidades_today':mensualidades_today,
		'egresos':egresos,
		'hoy':hoy,
		'hora':hora,
		'user' : request.user
	}
	return render(request, 'Caja/cierre.html', context)






#######################NUEVO INGRESO DE MENSUALIDAD###########################
@login_required(login_url = 'Panel:Login' )
def NewMensualIngreso(request):
	socio = tb_socio.objects.get(perfil__user__id = request.user.id)
	contexto = {
	'socio':socio,
	}
	return render(request, 'Caja/NuevoPagodeMensualidad.html', contexto)
	


@login_required(login_url = 'Panel:Login' )
def ListOtroIngresos(request):
	ingresos = tb_ingresos.objects.all()
	contexto = {
		'ingresos':ingresos
	}
	return render(request, 'Caja/OtroIngresosList.html', contexto)




@login_required(login_url = 'Panel:Login' )
def ListadoDeIngresos(request):
	ingresos = tb_ingreso_mensualidad.objects.all()
	contexto = {
	'ingresos':ingresos
	}
	return render(request, 'Caja/ListaDeCaja.html', contexto )

##########################PROCESANDO INGRESO###################################
def NuevoReporteDePagoMensual(request):
	usuario = request.GET.get('usuario', None)
	nombre = request.GET.get('nombre', None)
	apellido = request.GET.get('apellido', None)
	correo  = request.GET.get('correo', None)
	plan = request.GET.get('tarifaMensual', None)
	monto_plan = request.GET.get('MontoTafifaMensual', None)
	descripcion = request.GET.get('Direccion', None)
	NuevoIngresoMensual = tb_ingreso_mensualidad()
	NuevoIngresoMensual.user = User.objects.get(username = usuario)
	NuevoIngresoMensual.plan = tb_plan.objects.get(nombrePlan = plan)
	NuevoIngresoMensual.monto = monto_plan
	NuevoIngresoMensual.descripcion = descripcion
	NuevoIngresoMensual.nombre = nombre
	NuevoIngresoMensual.apellido = apellido
	NuevoIngresoMensual.correo = correo
	NuevoIngresoMensual.save()
	socio = tb_socio.objects.get(perfil__user__username = usuario)
	socio.status = 'Activo'
	fecha_de_desactivacion_vieja = socio.dateInactive_socio
	socio.dateInactive_socio = Desactivate_Register(fecha_de_desactivacion_vieja, 1)
	socio.save()
	MailNewIngresoMensualidad.delay(usuario,monto_plan,plan,correo)
	return HttpResponse(200)





def NewIngreso(request):
	Form = IngresoRegisterForm() 
	if request.method == 'POST':
		Form  = IngresoRegisterForm(request.POST, request.FILES  or None)
		if Form.is_valid():
			Form = Form.save(commit=False)
			Form.user = request.user
			Form.save()
			return redirect('Caja:ListOtroIngresos')
		else:
			print('error')
	else:
		pass
	contexto = {
		'Form':Form,
	}

	return render(request, 'Caja/newingreso.html', contexto)




###################################EGRESOS###############################################


@login_required(login_url = 'Panel:Login' )
def ListEgresos(request):
	egresos = tb_egreso.objects.all()
	contexto = {
		'egresos':egresos
	}
	return render(request, 'Caja/Egresos.html', contexto)




def NewEgreso(request):
	Form = EgresoRegisterForm() 
	colaboradores = tb_colaboradores.objects.all()
	proveedores = tb_proveedor.objects.all()

	if request.method == 'POST':
		print(request.POST)
		Form  = EgresoRegisterForm(request.POST, request.FILES  or None)
		if Form.is_valid():
			Form = Form.save(commit=False)
			Form.user = request.user
			if request.POST['proveedor'] != "":
				Form.proveedor = tb_proveedor.objects.get(id = request.POST['proveedor'])
			if request.POST['colaborador'] != "":
				colaborador = tb_colaboradores.objects.get(id = request.POST['colaborador'])
				Form.colaborador = colaborador
				colaborador.montoPagadoColaborador += float(request.POST['monto'])
				colaborador.cuentaColaborador -= float(request.POST['monto'])
				colaborador.save()
			Form.tipoDeEgreso = tb_tipoEgreso.objects.get(id= request.POST['tipoDeEgreso'])
			Form.save()
			return redirect('Caja:ListEgresos')
			print('ESTA GUARDADO')
		else:
			print('error')
	else:
		pass
	contexto = {
		'Form':Form,
		'colaboradores':colaboradores,
		'proveedores':proveedores
	}

	return render(request, 'Caja/newegreso.html', contexto)





def Resumen(request):
	ingresos = tb_ingreso_mensualidad.objects.all()
	ingresos_especial = tb_ingresos.objects.all()
	egresos = tb_egreso.objects.all()
	tipo_egreso = tb_tipoEgreso.objects.all()
	contexto = {
		'ingresos':ingresos,
		'ingresos_especial':ingresos_especial,
		'egresos':egresos,
		'tipo_egreso':tipo_egreso
	}
	return render(request, 'Caja/Resumen.html', contexto)






def QueryAnual(request):
	year = int(request.GET.get('year', None))
	all_objects = list(tb_ingresos.objects.filter(dateCreate__year = year)) + list(tb_ingreso_mensualidad.objects.filter(dateCreate__year = year)) + list(tb_egreso.objects.filter(dateCreate__year=year))
	data = serializers.serialize('json', all_objects)
	return HttpResponse(data)

def QueryMensual(request):
	year = int(request.GET.get('year', None))
	month = int(request.GET.get('month', None))
	all_objects = list(tb_ingresos.objects.filter(dateCreate__year = year).filter(dateCreate__month = month)) + list(tb_ingreso_mensualidad.objects.filter(dateCreate__year = year).filter(dateCreate__month = month)) + list(tb_egreso.objects.filter(dateCreate__year=year).filter(dateCreate__month = month))
	data = serializers.serialize('json', all_objects)
	return HttpResponse(data)

def QueryDia(request):
	dia = request.GET.get('dia', None)
	all_objects = list(tb_ingresos.objects.filter(dateCreate = dia)) + list(tb_ingreso_mensualidad.objects.filter(dateCreate = dia)) + list(tb_egreso.objects.filter(dateCreate = dia))
	data = serializers.serialize('json', all_objects)
	return HttpResponse(data)

def QueryTipoEgreso(request):
	year =int(request.GET.get('year', None))
	month = int(request.GET.get('month', None))
	tipo_egreso = request.GET.get('tipo_egreso', None)
	query = tb_egreso.objects.filter(dateCreate__year = year).filter(dateCreate__month = month).filter(tipoDeEgreso__tipodeEgreso = tipo_egreso)
	data = serializers.serialize('json', query)
	return HttpResponse(data)