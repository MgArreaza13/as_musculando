from django.core.mail import send_mail
from django.core.mail import send_mass_mail
from apps.UserProfile.models import tb_profile
from django.contrib.auth.models import User
from celery import task
from Musculando.celery import app
import time
import json
import logging
from apps.Panel.consumers import ws_connect
from channels import Group
from celery import task
from Musculando.celery import app
from datetime import datetime
from apps.tasks.Email_tasks import VencimientoMensualidad
from apps.Socios.models import tb_socio
from celery import shared_task






####################################MODELOS#########################################
from django.contrib.auth.models import User
from apps.Caja.models import tb_ingreso_mensualidad
from apps.Caja.models import tb_ingresos
from apps.Caja.models import tb_egreso


from apps.Configuracion.models import tb_plan
from apps.Configuracion.models import tb_formasDePago
from apps.Configuracion.models import tb_tipoColaborador
from apps.Configuracion.models import tb_tipoEgreso
from apps.Configuracion.models import tb_tipoIngreso

from channels import Channel
log = logging.getLogger(__name__)


@app.task 
def ActualizacionDeUsuarios():
	ingresos_mensualidad = tb_ingreso_mensualidad.objects.filter(user__username = 'demo')
	for i in range(0, len(ingresos_mensualidad)):
		ingresos_mensualidad[i].user = User.objects.get(username = 'Peca_Operador')
		ingresos_mensualidad[i].save()

	ingresos = tb_ingresos.objects.filter(user__username = 'demo')
	for i in range(0, len(ingresos)):
		ingresos[i].user = User.objects.get(username = 'Peca_Operador')
		ingresos[i].save()

	egresos = tb_egreso.objects.filter(user__username = 'demo')
	for i in range(0, len(egresos)):
		egresos[i].user = User.objects.get(username = 'Peca_Operador')
		egresos[i].save()

	planes = tb_plan.objects.filter(user__username = 'demo')
	for i in range(0, len(planes)):
		planes[i].user = User.objects.get(username = 'Peca_Operador')
		planes[i].save()

	formasdepago = tb_formasDePago.objects.filter(user__username = 'demo')
	for i in range(0, len(formasdepago)):
		formasdepago[i].user = User.objects.get(username = 'Peca_Operador')
		formasdepago[i].save()

	tipodecolaboradores = tb_tipoColaborador.objects.filter(user__username = 'demo')
	for i in range(0, len(tipodecolaboradores)):
		tipodecolaboradores[i].user = User.objects.get(username = 'Peca_Operador')
		tipodecolaboradores[i].save()

	tipodeegresos = tb_tipoEgreso.objects.filter(user__username = 'demo')
	for i in range(0, len(tipodeegresos)):
		tipodeegresos[i].user = User.objects.get(username = 'Peca_Operador')
		tipodeegresos[i].save()

	tipodeingresos = tb_tipoIngreso.objects.filter(user__username = 'demo')
	for i in range(0, len(tipodeingresos)):
		tipodeingresos[i].user = User.objects.get(username = 'Peca_Operador')
		tipodeingresos[i].save()





@app.task
def Socios():
	#print('migueeeeeeeeeeel')
	hoy = datetime.today().date()
	socios = tb_socio.objects.all()
	for i in range(0,len(socios)):
	#	print(i)
		if(socios[i].dateInactive_socio == hoy):
			socios[i].status = 'Desactivado'
			socios[i].save()
			#print(socios[i])
			VencimientoMensualidad(socios[i].perfil.nameUser, socios[i].TarifaMensual.precioPlan, socios[i].TarifaMensual.nombrePlan, socios[i].perfil.mailUser)


