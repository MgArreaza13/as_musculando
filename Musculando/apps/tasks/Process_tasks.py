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

from channels import Channel
log = logging.getLogger(__name__)



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


