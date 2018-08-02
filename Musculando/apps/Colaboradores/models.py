from django.db import models
from django.conf import settings
from apps.Configuracion.models import tb_tipoColaborador
from apps.UserProfile.models import tb_profile
import time

#from apps.Turn.models import tb_status_turn

# Create your models here.

PAGO_CHOICES = (
    ('Honorarios Mensuales', 'Honorarios Mensuales'),
    ('Monto Por Clase', 'Monto Por clase'),
	('Sin Definir', 'Sin Definir'),
    ('Comision Por Clase', 'Comision Por Clase'),
    ('Presentimo', 'Presentimo'),
    ('Aguinaldo', 'Aguinaldo'),
    ('Liquidacion Mensual', 'Liquidacion Mensual'),

)
class tb_colaboradores (models.Model):
	user						=	models.OneToOneField(tb_profile, on_delete=models.CASCADE, null=True)
	honorariosMensuales			=	models.FloatField(default=0, null=True, max_length=300)
	montoXClase					=	models.FloatField(default=0, null=True, max_length=300)
	comisionXClase				=	models.FloatField(default=0, null=True, max_length=300)
	presentimo					=	models.FloatField(default=0, null=True, max_length=300)
	montoAguinaldo				=	models.FloatField(default=0, null=True, max_length=300)
	tipoColaborador				=	models.ForeignKey(tb_tipoColaborador, on_delete=models.CASCADE, null=False, default='')
	cuentaColaborador			=	models.FloatField(default=0, null=True, max_length=300)
	montoPagadoColaborador 		=	models.FloatField(default=0, null=True, max_length=300)
	isHonorarios				=   models.BooleanField(null=False, blank=True , default=False)
	isMontoXClase				=   models.BooleanField(null=False, blank=True , default=False)
	isComison					=   models.BooleanField(null=False, blank=True , default=False)
	isPresentimo				=   models.BooleanField(null=False, blank=True , default=False)
	isPresentimoPay				=   models.BooleanField(null=False, blank=True , default=False)
	isAguinaldo					=   models.BooleanField(null=False, blank=True , default=False)
	isHonorariosUpload			=   models.BooleanField(null=False, blank=True , default=False)
	dateCreate					=	models.DateField(auto_now=True, blank=False)

	#diasParaElPremio	= 	models.CharField(default='0', null=True, max_length=30)
	#nameUser		=	models.CharField(default='Sin Definir', null=True, max_length=30)
	#lastName		=	models.CharField(default='Sin Definir', null=True, max_length=30)
	#dni 			=	models.CharField(default='A-000000000', null=True, max_length=30)
	#movilTlf		=	models.CharField(default='+000000000', null=True, max_length=30)
	#houseTlf		=	models.CharField(default='+000000000', null=True, max_length=30)
	#mailUser		=	models.EmailField(default='sin@definir.com', null=True, max_length=30)
	#birthdayDate	=	models.DateField(blank=False, null=True, default='1995-04-19' )
	#image 			= 	models.ImageField(upload_to='users/avatar/', default='', null=False, )
	#image 			= 	models.ImageField(upload_to='users/avatar/', default='', null=True, )
	#tipoUser		=  	models.CharField(max_length=30,null=False,choices=PAGO_CHOICES,default='SinDefinir',) # Esto se utilizara para saber si es admin, colaborador o client
	#is_complete		=   models.BooleanField(null=False, blank=True , default=False)
	#nameProfile	=	models.CharField(default='', null=False, max_length=30)
	#StatusKf		= 	models.ForeignKey(tb_status_turn, on_delete=models.CASCADE, null=False, default='')
	def __str__(self):
		return self.user.nameUser
	class Meta:
		managed = True
		db_table = 'colaboradores'


class tb_cuentaColaborador (models.Model):
	#user					=	models.OneToOneField(tb_profile, on_delete=models.CASCADE, null=True)
	colaborador				=	models.ForeignKey(tb_colaboradores, on_delete=models.CASCADE, null=False, default='')
	typePago				=	models.CharField(max_length=300,null=False,choices=PAGO_CHOICES,default='SinDefinir',)
	monto					=	models.FloatField(default=0, null=True, max_length=300)
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	
	def __str__(self):
		return self.colaborador.user.nameUser
	class Meta:
		managed = True
		db_table = 'cuentaColaborador'


Entrada_CHOICES = (
    ('Entrada', 'Entrada'),
    ('Salida', 'Salida'),

)




def get_default_my_hour():
	return time.strftime("%H:%M:%S")

class tb_EntradaSalida (models.Model):
	#user					=	models.OneToOneField(tb_profile, on_delete=models.CASCADE, null=True)
	colaborador				=	models.ForeignKey(tb_colaboradores, on_delete=models.CASCADE, null=False, default='')
	typeEntradaSalida		=   models.CharField(max_length=300,null=False,choices=Entrada_CHOICES,default='Entrada',)
	hora					= 	models.CharField(max_length=50, default=get_default_my_hour) 
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	
	def __str__(self):
		return self.colaborador.user.nameUser
	class Meta:
		managed = True
		db_table = 'EntradaSalida'