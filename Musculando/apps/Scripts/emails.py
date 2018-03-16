from django.core.mail import send_mail
from django.core.mail import send_mass_mail

def MailNewIngresoMensualidad(self, usuario, correo):
	cuerpo = ""
	servicios = request.GET.get('servicios', None)
	email_subject_usuario = 'Musculando - Reporte de Pago de Mensualidad'
	email_body_usuario = "Hola %s, hemos recidido satisfactoriamente su pago por lo que menos activado su perfil nuevamente, disfrute de nuestros servicios al maximo, gracias" %(usuario)
	message_usuario = (email_subject_usuario, email_body_usuario , 'musculando@b7000615.ferozo.com', [correo])
	#mensaje para apreciasoft
	email_subject_Soporte = 'Multipoint - Nueva Cotizacion NO CONCRETADA'
	email_body_Soporte = "se ha registrado  una  visita de un cliente y no concreto la reserva sus datos son  , nombre:%s . correo:%s, numero:%s habia solicitado un evento de %s y servicios de %s con un monto total de $%s " %(nombre, correo, numero, evento, servicios, monto)
	send_mail(email_subject_Soporte, cuerpo , 'musculando@b7000615.ferozo.com', ['soporte@apreciasoft.com', "mg.arreaza.13@gmail.com", 'reservas@boomeventos.com'],fail_silently=True, html_message=email_body_Soporte)
	#enviamos el correo
	send_mass_mail((message_usuario), fail_silently=False)