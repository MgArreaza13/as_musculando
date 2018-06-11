from django.db import models

##############MODELOS EXTERNOS################
from apps.Configuracion.models import tb_plan
from apps.UserProfile.models import tb_profile


# Create your models here.
PAGO_CHOICES = (
    ('Activo', 'Activo'),
	('Pendiente', 'Pendiente'),
    ('Desactivado', 'Desactivado'),
    #('Cliente', 'Cliente'),
    #('Socio', 'Socio'),
)
class tb_socio (models.Model):
	perfil						=	models.OneToOneField(tb_profile, on_delete=models.CASCADE, null=False, default='')
	obraSocial					=	models.CharField(default='Sin Definir', null=True, max_length=30)
	status						=	models.CharField(max_length=30,null=False,choices=PAGO_CHOICES,default='Pendiente',)
	TarifaMensual 				=	models.ForeignKey(tb_plan, on_delete=models.CASCADE, null=True, default='')
	#movilTlf					=	models.CharField(default='+000000000', null=True, max_length=30)
	#houseTlf					=	models.CharField(default='+000000000', null=True, max_length=30)
	#mailUser					=	models.EmailField(default='sin@definir.com', null=True, max_length=30)
	#birthdayDate				=	models.DateField(blank=False, null=True, default='1995-04-19' )
	#image 						= 	models.ImageField(upload_to='users/avatar/', default='', null=False, )
	#image 						= 	models.ImageField(upload_to='users/avatar/', default='', null=True, )
	#tipoUser					=  	models.CharField(max_length=30,null=False,choices=PAGO_CHOICES,default='SinDefinir',) # Esto se utilizara para saber si es admin, colaborador o client
	dateInactive_socio			=	models.DateField(blank=False, null=True, default='2018-04-19' )
	dateCreate_socio			=	models.DateField(auto_now=True, blank=False)
	#is_complete				=   models.BooleanField(null=False, blank=True , default=False)
	#nameProfile				=	models.CharField(default='', null=False, max_length=30)
	#StatusKf					= 	models.ForeignKey(tb_status_turn, on_delete=models.CASCADE, null=False, default='')
	def __str__(self):
		return self.perfil.nameUser
	class Meta:
		managed = True
		db_table = 'socios'