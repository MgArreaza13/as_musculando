from django.db import models
from apps.Configuracion.models import tb_turn_sesion
# Create your models here.


STATE_RESERVAS = (
    ('Confirmada', 'Confirmada'),
    ('En Espera', 'En Espera'),
    ('No Aprobada', 'No Aprobada'),
)



class Cancha(models.Model):
	nameCancha					=	models.CharField(default='Sin Datos', null=True, max_length=300)
	precioHora					=	models.FloatField(default='0', null=True,)
	description					=	models.TextField(default='Sin Datos', null=True)
	image 						= 	models.ImageField(upload_to='cancha/img/', default='', null=True, )
	#phoneNumberProveedor		=	models.CharField(default='+000000000', null=True, max_length=30)
	#email 						= 	models.EmailField(default='sin@datos.com', null=True, max_length=30)
	dateCreate					=	models.DateField(auto_now=True, blank=False)
	def __str__(self):
		return self.nameCancha
	class Meta:
		managed = True
		db_table = 'canchas'



class ReservaCancha(models.Model):
	mail					=  	models.EmailField(default='', null=False, max_length=30)
	nombre					= 	models.CharField(default='', null=False, max_length=30)
	telefono				=	models.CharField(default='', null=False, max_length=30)
	statusTurn 				=	models.CharField(max_length=255,null=False,choices=STATE_RESERVAS,default='En Espera',)
	turn 					=   models.ForeignKey(tb_turn_sesion, on_delete=models.CASCADE, default='', blank=True)
	cancha					=	models.ForeignKey(Cancha, on_delete=models.CASCADE, null=False, default='')
	dateTurn				=	models.DateField(auto_now=False, auto_now_add=False, null=False, default='' , blank=True)
	montoAPagar				=   models.IntegerField(default=0, null=False, blank=True)
	montoPagado				=   models.IntegerField(default=0, null=True, blank=True)
	isPay			 		=	models.BooleanField(null=False, blank=True , default=False)
	description				=	models.TextField(default='Sin Descripcion', null=False, max_length=3000000, blank=True)	
	TipoReservas			=   models.CharField(default='Reserva Web', null=True, max_length=30)
	observaciones           =  	models.TextField(default='Sin Obsevaciones', null=False, max_length=3000)
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	def __str__(self):
		return self.nombre
	class Meta:
		managed = True
		db_table = 'ReservaCancha'

	
	#precioHora					=	models.FloatField(default='0', null=True,)
	#description					=	models.TextField(default='Sin Datos', null=True)
	#image 						= 	models.ImageField(upload_to='cancha/img/', default='', null=True, )
	#phoneNumberProveedor		=	models.CharField(default='+000000000', null=True, max_length=30)
	#email 						= 	models.EmailField(default='sin@datos.com', null=True, max_length=30)
	#dateCreate					=	models.DateField(auto_now=True, blank=False)
	#servicioPrestar			= 	models.ForeignKey(tb_product,on_delete=models.CASCADE, null=True, default='')
	#dateTurn				=	models.DateField(auto_now=False, auto_now_add=False, null=False, default='' , blank=True)
	#turn 					=   models.ForeignKey(tb_turn_sesion, on_delete=models.CASCADE, default='', blank=True)
	#mail					=  	models.EmailField(default='', null=False, max_length=30)
	#nombre					= 	models.CharField(default='', null=False, max_length=30)
	#telefono				=	models.CharField(default='', null=False, max_length=30)
	#statusTurn 				=	models.ForeignKey(tb_status, on_delete=models.CASCADE, null=False, default='')
	#montoAPagar				=   models.IntegerField(default=0, null=False, blank=True)
	#montoPagado				=   models.IntegerField(default=0, null=True, blank=True)
	#isPay			 		=	models.BooleanField(null=False, blank=True , default=False)
	#description				=	models.TextField(default='Sin Descripcion', null=False, max_length=3000000, blank=True)	
	#ingenico_id             =  	models.TextField(default='None', null=False, max_length=3000)
	#PagoOnline			 	=	models.BooleanField(null=False, blank=True , default=False)
	#TipoReservas			=   models.CharField(default='Reserva Web', null=True, max_length=30)
	#observaciones           =  	models.TextField(default='Sin Obsevaciones', null=False, max_length=3000)
	