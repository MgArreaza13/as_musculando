from django.db import models
from django.conf import settings
#from apps.Turn.models import tb_status_turn

# Create your models here.

PAGO_CHOICES = (
    ('Administrador', 'Administrador'),
    ('Colaborador', 'Colaborador'),
	('SinDefinir', 'Sin Definir'),
    ('Socio', 'Socio'),
)
class tb_profile (models.Model):
	user			=	models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
	nameUser		=	models.CharField(default='Sin Definir', null=True, max_length=300)
	lastName		=	models.CharField(default='Sin Definir', null=True, max_length=300)
	dni 			=	models.CharField(default='A-000000000', null=True, max_length=30)
	movilTlf		=	models.CharField(default='+000000000', null=True, max_length=30)
	houseTlf		=	models.CharField(default='+000000000', null=True, max_length=30)
	mailUser		=	models.EmailField(default='sin@definir.com', null=True, max_length=300)
	birthdayDate	=	models.DateField(blank=False, null=True, default='1995-04-19' )
	#image 			= 	models.ImageField(upload_to='users/avatar/', default='', null=False, )
	image 			= 	models.ImageField(upload_to='users/avatar/', default='', null=True, )
	tipoUser		=  	models.CharField(max_length=30,null=False,choices=PAGO_CHOICES,default='SinDefinir',) # Esto se utilizara para saber si es admin, colaborador o client
	dateCreate		=	models.DateField(auto_now=True, blank=False)
	is_complete		=   models.BooleanField(null=False, blank=True , default=False)
	#nameProfile	=	models.CharField(default='', null=False, max_length=30)
	#StatusKf		= 	models.ForeignKey(tb_status_turn, on_delete=models.CASCADE, null=False, default='')
	def __str__(self):
		return self.nameUser
	class Meta:
		managed = True
		db_table = 'profile'