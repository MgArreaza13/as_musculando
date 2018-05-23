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

from channels import Channel
log = logging.getLogger(__name__)


#######################ENVIAR CORREO CUANDO REPORTA PAGO#################################
@app.task
def MailNewIngresoMensualidad(usuario, monto, plan, correo):
	cuerpo = ""
	###Mensaje para el usuario #########
	email_subject_usuario = 'Musculando - Reporte de Pago de Mensualidad'
	email_body_usuario = "Hola %s, hemos recidido satisfactoriamente su pago por lo que menos activado su perfil nuevamente, disfrute de nuestros servicios al maximo, gracias" %(usuario)
	send_mail (email_subject_usuario, cuerpo, 'musculando@b7000615.ferozo.com', [correo], fail_silently=True, html_message=email_body_usuario)
	#mensaje para apreciasoft
	email_subject_Soporte = 'Musculando - Nueva pago de Mensualidad'
	email_body_Soporte = "Se ha registrado un pago de mensualidad en el sistema por el socio %s y un monto de $:%s referente al plan %s y por ende lo hemos activado satisfactoriamente" %(usuario,monto,plan)
	send_mail(email_subject_Soporte, cuerpo , 'musculando@b7000615.ferozo.com', ['soporte@apreciasoft.com', "mg.arreaza.13@gmail.com",],fail_silently=True, html_message=email_body_Soporte)
	




##################EMAIL PARA SOCIO DESACTIVADO POR FECHA VENCIMIENTO #########################

@app.task
def VencimientoMensualidad(usuario, monto, plan, correo):
	cuerpo = ""
	###Mensaje para el usuario #########
	email_subject_usuario = 'Musculando - Desactivacion de Perfil'
	email_body_usuario = "Hola %s, Hemos desactivado tu perfil porque se ha vencido tu cuota mensual, te invitamos a ingresar al sistema y poder solicitar tu activacion reportando el pago correspondiente a tu plan" %(usuario)
	send_mail (email_subject_usuario, cuerpo, 'musculando@b7000615.ferozo.com', [correo], fail_silently=True, html_message=email_body_usuario)
	#mensaje para apreciasoft
	email_subject_Soporte = 'Musculando - Desactivacion de Perfil Por vencimiento de cuota'
	email_body_Soporte = "Hemos desactivado el socio %s por vencimiendo , esperemos reporte el pago por un monto de $:%s referente al plan %s te informaremos a penas solicite la activacion" %(usuario,monto,plan)
	send_mail(email_subject_Soporte, cuerpo , 'musculando@b7000615.ferozo.com', ['soporte@apreciasoft.com', "mg.arreaza.13@gmail.com",],fail_silently=True, html_message=email_body_Soporte)
	


##################EMAIL NUEVO SOCIO #########################

@app.task
def NewSocioMAil(usuario, monto, plan, correo, ):
	time.sleep(40)
	cuerpo = ""
	###Mensaje para el usuario #########
	email_subject_usuario = 'Musculando - Bienvenido a la Familia Musculando'
	email_body_usuario = "Hola %s, hemos creado tu perfil perfectamente y nos complace darte la bienvenida a esta gran familia , disfruta de las ventajas de Musculando." %(usuario)
	send_mail (email_subject_usuario, cuerpo, 'musculando@b7000615.ferozo.com', [correo], fail_silently=True, html_message=email_body_usuario)
	#mensaje para apreciasoft
	email_subject_Soporte = 'Musculando - Nuevo Socio Creado '
	email_body_Soporte = "Hemos creado el socio %s perfectamente un monto de $:%s referente al plan %s " %(usuario,monto,plan)
	send_mail(email_subject_Soporte, cuerpo , 'musculando@b7000615.ferozo.com', ['soporte@apreciasoft.com', "mg.arreaza.13@gmail.com",],fail_silently=True, html_message=email_body_Soporte)
	Group('notifcaciones').send({
        'text': json.dumps ({"action": "completed","content": "Hemos Finalizado el proceso"})
    })
##################EMAIL PARA SOCIO DESACTIVADO #########################

@app.task
def DesactivacionSocio(usuario, monto, plan, correo):
	cuerpo = ""
	###Mensaje para el usuario #########
	email_subject_usuario = 'Musculando - Desactivacion de Perfil'
	email_body_usuario = "Hola %s, Hemos desactivado tu perfil porque asi lo solicito el administrador, te invitamos a ingresar al sistema y poder solicitar tu activacion reportando el pago correspondiente a tu plan" %(usuario)
	send_mail (email_subject_usuario, cuerpo, 'musculando@b7000615.ferozo.com', [correo], fail_silently=True, html_message=email_body_usuario)
	#mensaje para apreciasoft
	email_subject_Soporte = 'Musculando - Desactivacion de Perfil Por vencimiento de cuota'
	email_body_Soporte = "Hemos desactivado el socio %s por tu solicitud , esperemos reporte el pago por un monto de $:%s referente al plan %s te informaremos a penas solicite la activacion" %(usuario,monto,plan)
	send_mail(email_subject_Soporte, cuerpo , 'musculando@b7000615.ferozo.com', ['soporte@apreciasoft.com', "mg.arreaza.13@gmail.com",],fail_silently=True, html_message=email_body_Soporte)
	



##################EMAIL PARA Activacion #########################

@app.task
def ActivacionSocio(usuario ,correo):
	cuerpo = ""
	###Mensaje para el usuario #########
	email_subject_usuario = 'Musculando - Activacion de Perfil'
	email_body_usuario = "Hola %s, Hemos Activado tu perfil porque asi lo solicito el administrador, Disfruta de nuestros beneficios nuevamente" %(usuario)
	send_mail (email_subject_usuario, cuerpo, 'musculando@b7000615.ferozo.com', [correo], fail_silently=True, html_message=email_body_usuario)
	#mensaje para apreciasoft
	email_subject_Soporte = 'Musculando - Activacion del perfil'
	email_body_Soporte = "Hemos Activado el socio %s respondiendo a tu solicitud de activacion satisfactoriamente," %(usuario)
	send_mail(email_subject_Soporte, cuerpo , 'musculando@b7000615.ferozo.com', ['soporte@apreciasoft.com', "mg.arreaza.13@gmail.com",],fail_silently=True, html_message=email_body_Soporte)
	



##################EMAIL POR ELIMINACION DE PERFIL #########################

@app.task
def PerfilEliminado():
	cuerpo = ""
	###Mensaje para el usuario #########
	
	#email_subject_usuario = 'Musculando - Perfil Eliminado'
	#email_body_usuario = "Hola %s, Hemos eliminado tu perfil lamentablemente por solicitud del administrador, contactate con el para verificar el porque se te ha borrado el perfil" %(usuario)
	#send_mail (email_subject_usuario, cuerpo, 'musculando@b7000615.ferozo.com', [correo], fail_silently=True, html_message=email_body_usuario)
	#mensaje para apreciasoft
	email_subject_Soporte = 'Musculando - Perfil Eliminado'
	email_body_Soporte = "Hemos Eliminado un socio  por solicitud de usted." 
	send_mail(email_subject_Soporte, cuerpo , 'musculando@b7000615.ferozo.com', ['soporte@apreciasoft.com', "mg.arreaza.13@gmail.com",],fail_silently=True, html_message=email_body_Soporte)
	




##################EMAIL POR ELIMINACION DE PERFIL BUSQUEDA DEL USUARIO #########################

@app.task
def GetProfile(id_user):
	queryset = User.objects.get(id = id_user)
	perfil = tb_profile.objects.get(user__username = queryset.username )
	PerfilEliminado.delay(perfil.nameUser, perfil.mailUser)
	






##################EMAIL POR ELIMINACION DE COLABORADOR #########################

@app.task
def ColaboradorEliminado():
	cuerpo = ""
	###Mensaje para el usuario #########
	
	#email_subject_usuario = 'Musculando - Perfil Eliminado'
	#email_body_usuario = "Hola %s, Hemos eliminado tu perfil lamentablemente por solicitud del administrador, contactate con el para verificar el porque se te ha borrado el perfil" %(usuario)
	#send_mail (email_subject_usuario, cuerpo, 'musculando@b7000615.ferozo.com', [correo], fail_silently=True, html_message=email_body_usuario)
	#mensaje para apreciasoft
	email_subject_Soporte = 'Musculando - Colaborador Eliminado'
	email_body_Soporte = "Hemos Eliminado un Colaborador  por solicitud de usted." 
	send_mail(email_subject_Soporte, cuerpo , 'musculando@b7000615.ferozo.com', ['soporte@apreciasoft.com', "mg.arreaza.13@gmail.com",],fail_silently=True, html_message=email_body_Soporte)
	


