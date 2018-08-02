##################tarea periodica de desactivar socio ################
from celery import task
from Musculando.celery import app
from datetime import datetime
from apps.Colaboradores.models import tb_colaboradores
from apps.Colaboradores.models import tb_cuentaColaborador
from apps.Configuracion.models import tb_tipoEgreso
from apps.tasks.Email_tasks import PagoColaborador
from apps.tasks.Email_tasks import AguinaldoColaborador
from apps.tasks.Email_tasks import administradorNotificacion
from apps.tasks.Email_tasks import administradorNotificacionPresentimo
from apps.tasks.Email_tasks import PresentimoColaborador
from apps.tasks.Email_tasks import administradorNotificacionAguinaldo
from apps.tasks.Email_tasks import administradorNotificacionHonorarios
from apps.tasks.Email_tasks import HonarariosMailColaborador
from apps.Caja.models import tb_egreso
from django.contrib.auth.models import User
from celery import shared_task
from apps.Panel.consumers import ws_connect
from channels import Group
import time
import json


from channels import Channel



#######################TAREAS PERIODICA ###########################
@app.task
def aguinaldo():
	 mes = datetime.today().month
	 dia = datetime.today().day

	 if(dia == 1 and mes == 5 or dia ==1 and mes == 12):
	 	#####mes de aguinaldo mayo, diciembre 
	 	########sumara el monto del aguinaldo a la cuenta del colaborador
	 	colaboradores =  tb_colaboradores.objects.all()
	 	for i in range(0, len(colaboradores)):
	 		if(colaboradores[i].isAguinaldo == True):
	 			#####verifico que el colaborador tenga habilitado el 
	 			#####aguinaldo si es asi, entonces sumare el monto a su cuenta 
	 			#####y lo registrare 
	 			colaboradores[i].cuentaColaborador += colaboradores[i].montoAguinaldo
	 			colaboradores[i].save()
	 			AguinaldoColaborador.delay(colaboradores[i].user.nameUser, colaboradores[i].user.mailUser)
	 			#######creo el registro del movimiento
	 			registro = tb_cuentaColaborador()
	 			registro.colaborador = tb_colaboradores.objects.get(id = colaboradores[i].id)
	 			registro.typePago = 'Aguinaldo'
	 			registro.monto = colaboradores[i].montoAguinaldo
	 			registro.save()
	 			administradorNotificacionAguinaldo.delay()








####################################presentimo################################################
@app.task
def SueldoMensual():
	time.sleep(15)
	colaboradores =  tb_colaboradores.objects.filter(isHonorarios =  True)
	dia = datetime.today().day
	if(dia == 1 or dia ==2 or dia == 3): #el dos es de debug pero tiene que ser solamente el 1
	 	#####mes de aguinaldo mayo, diciembre 
	 	########sumara el monto del aguinaldo a la cuenta del colaborador
	 	for i in range(0, len(colaboradores)):	
	 		if colaboradores[i].isHonorariosUpload == False:
	 			#####verifico que el colaborador tenga habilitado el 
		 		#####aguinaldo si es asi, entonces sumare el monto a su cuenta 
		 		#####y lo registrare 
		 		colaboradores[i].cuentaColaborador += colaboradores[i].honorariosMensuales
		 		colaboradores[i].isHonorariosUpload = True
		 		colaboradores[i].save()
		 		HonarariosMailColaborador.delay(colaboradores[i].user.nameUser, colaboradores[i].user.mailUser)
		 		#######creo el registro del movimiento
		 		registro = tb_cuentaColaborador()
		 		registro.colaborador = tb_colaboradores.objects.get(id = colaboradores[i].id)
		 		registro.typePago = 'Honorarios Mensuales'
		 		registro.monto = colaboradores[i].honorariosMensuales
		 		registro.save()
		 		administradorNotificacionHonorarios.delay()
		 	else:
		 		pass






@app.task
def presentimo():
	time.sleep(15) 
	colaboradores =  tb_colaboradores.objects.filter(isPresentimo =  True)
	for i in range(0, len(colaboradores)):
		#####verifico que el colaborador tenga habilitado el 
		#####aguinaldo si es asi, entonces sumare el monto a su cuenta 
		#####y lo registrare 
		colaboradores[i].cuentaColaborador += colaboradores[i].presentimo
		colaboradores[i].isPresentimoPay =  True
		colaboradores[i].save()
		#####correo al colaborador 
		PresentimoColaborador.delay(colaboradores[i].user.nameUser, colaboradores[i].user.mailUser)
		#######creo el registro del movimiento
		registro = tb_cuentaColaborador()
		registro.colaborador = tb_colaboradores.objects.get(id = colaboradores[i].id)
		registro.typePago = 'Presentimo'
		registro.monto = colaboradores[i].presentimo
		registro.save()

	 ########correo al administrador 
	administradorNotificacionPresentimo.delay()
	Group('notifcaciones').send({'text': json.dumps ({"action": "presentimo","content": "Hemos Finalizado el proceso de pago de presentimo"})})




############################pago a todos los colaboradores###################################
@app.task
def LiquidacionColaboradores(usuario_id):
	#####pagar el monto de cada colaborador 
	time.sleep(10) 
	colaborador  = tb_colaboradores.objects.all()
	for i in range(0,len(colaborador)):
		monto = colaborador[i].cuentaColaborador
		if (monto > 0 ):
			colaborador[i].montoPagadoColaborador += colaborador[i].cuentaColaborador
			colaborador[i].cuentaColaborador -= colaborador[i].cuentaColaborador
			colaborador[i].save()
			PagoColaborador.delay(colaborador[i].user.nameUser, colaborador[i].user.mailUser)
			##### registrarlo en su cuenta
			#registro = tb_cuentaColaborador()
		 	#registro.colaborador = tb_colaboradores.objects.get(id = colaboradores[i].id)
		 	#registro.typePago = 'Liquidacion Mensual'
		 	#registro.monto = colaboradores[i].montoAguinaldo
		 	#registro.save() 
			#### y registrarlo en egresos
			egreso = tb_egreso()
			egreso.user = User.objects.get(id = usuario_id)
			egreso.monto = monto
			egreso.descripcion = 'Pago de Colaborador'
			egreso.tipoDeEgreso = tb_tipoEgreso.objects.get(  tipodeEgreso = 'Pago Colaboradores')
			egreso.colaborador = tb_colaboradores.objects.get(id = colaborador[i].id)
			egreso.save()
	#### responder con channels para activar la notificacion de escritorio
	#### Enviar correo
	administradorNotificacion.delay()
	Group('notifcaciones').send({
		        'text': json.dumps ({"action": "liquidacion","content": "Hemos Finalizado el proceso de pago"})
		    })
			
	


@app.task
def PresentimoMensualActivate():
	dia = datetime.today().day
	if (dia == 1):
		colaboradores = tb_colaboradores.objects.filter(isPresentimo =  True)
		for i in range(0, len(colaboradores)):
			colaboradores[i].isPresentimoPay =  False
			colaboradores[i].save()
