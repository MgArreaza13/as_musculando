from django.shortcuts import render
from django.contrib.auth.models import User 
from django.http import HttpResponse
#################MODELOS###################
from apps.Socios.models import tb_socio
from apps.Caja.models import tb_ingreso_mensualidad
from apps.Configuracion.models import tb_plan
from django.contrib.auth.decorators import login_required
################SCRIPTS#########################
from apps.Scripts.DesactivateUser import Desactivate_Register
# Create your views here.

#################tareas asincronas correos ##########################
from apps.tasks.Email_tasks import MailNewIngresoMensualidad

#######################NUEVO INGRESO DE MENSUALIDAD###########################
@login_required(login_url = 'Panel:Login' )
def NewMensualIngreso(request):
	socio = tb_socio.objects.get(perfil__user__id = request.user.id)
	contexto = {
	'socio':socio,
	}
	return render(request, 'Caja/NuevoPagodeMensualidad.html', contexto)
	
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