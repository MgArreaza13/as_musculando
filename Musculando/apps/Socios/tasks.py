##################tarea periodica de desactivar socio ################
from celery import task
from Musculando.celery import app
from datetime import datetime
from apps.tasks.Email_tasks import VencimientoMensualidad
from apps.Socios.models import tb_socio
from celery import shared_task
from apps.tasks.Process_tasks import Socios


#######################TAREAS PERIODICA ###########################
@app.task
def desactivatesocios():
	#print('migueeeeeeeeeeel')
	hoy = datetime.today().date()
	socios = tb_socio.objects.all()
	for i in range(0,len(socios)):
		#print(i)
		if(socios[i].dateInactive_socio == hoy and socios[i].status == 'Activo'):
			socios[i].status = 'Desactivado'
			socios[i].save()
			#print(socios[i])
			VencimientoMensualidad.delay(socios[i].perfil.nameUser, socios[i].TarifaMensual.precioPlan, socios[i].TarifaMensual.nombrePlan, socios[i].perfil.mailUser)

