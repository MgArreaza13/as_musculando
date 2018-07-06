from django.shortcuts import render
from django.contrib.auth.models import User 
from django.http import HttpResponse
from django.shortcuts import redirect
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
	contexto = {
		'ingresos':ingresos,
		'ingresos_especial':ingresos_especial,
		'egresos':egresos
	}
	return render(request, 'Caja/Resumen.html', contexto)