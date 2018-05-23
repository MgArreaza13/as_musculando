from django.db import models
from django.conf import settings
from apps.Configuracion.models import tb_plan
from apps.Configuracion.models import tb_tipoEgreso
from apps.Proveedores.models import tb_proveedor
# Create your models here.

class tb_ingreso_mensualidad (models.Model):
	user 					=	models.ForeignKey(settings.AUTH_USER_MODEL)
	plan					=	models.ForeignKey(tb_plan, on_delete=models.CASCADE, null=True,)
	#turno					=   models.ForeignKey(tb_turn, on_delete=models.CASCADE, null=True,)
	#tipoPago				=	models.ForeignKey(tb_formasDePago, on_delete=models.CASCADE, null=True, default='')
	#tipoIngreso			=	models.ForeignKey(tb_tipoIngreso, on_delete=models.CASCADE, null=True, default='')
	#service				=	models.ForeignKey(tb_service, on_delete=models.CASCADE, null=True, default='')
	monto					=	models.IntegerField(default='0000', null=True,)
	descripcion	 			=	models.TextField(default='Sin Descripcion', null=True, max_length=3000)
	nombre					=	models.CharField(default='Sin nombre', null=False, max_length=300)
	apellido					=	models.CharField(default='Sin Apellido', null=False, max_length=300)
	correo					=	models.EmailField(default='sin@email.com', null=False, max_length=30)
	#CollaboratorFavoriteKf	= 	models.ForeignKey(tb_collaborator, on_delete=models.CASCADE, null=False, default='')
	#addressClientTwo		= 	models.TextField(default='', null=False)
	#isSendPromotions		=	models.BooleanField()
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	#isVip					= 	models.BooleanField()
	#StatusKf				=	models.ForeignKey(tb_status_turn, on_delete=models.CASCADE, null=False, default='')
	#TypeClienteKf			=	models.ForeignKey(tb_type_client, on_delete=models.CASCADE, null=False, default='')
	def __str__(self):
		return self.user.username
	class Meta:
		managed = True
		db_table = 'ingreso_mensualidad' 




class tb_egreso(models.Model):
	user 							=	models.ForeignKey(settings.AUTH_USER_MODEL)
	monto							=	models.IntegerField(default='0000', null=True,)
	descripcion	 					=	models.TextField(default='Sin Descripcion', null=True, max_length=3000)
	proveedor						=	models.ForeignKey(tb_proveedor, on_delete=models.CASCADE, null=True,)
	tipoDeEgreso					=   models.ForeignKey(tb_tipoEgreso, on_delete=models.CASCADE, null=True,)
	#tipoPago				=	models.ForeignKey(tb_formasDePago, on_delete=models.CASCADE, null=True, default='')
	#tipoIngreso			=	models.ForeignKey(tb_tipoIngreso, on_delete=models.CASCADE, null=True, default='')
	#service				=	models.ForeignKey(tb_service, on_delete=models.CASCADE, null=True, default='')
	#nombre					=	models.CharField(default='Sin nombre', null=False, max_length=300)
	#apellido					=	models.CharField(default='Sin Apellido', null=False, max_length=300)
	#correo					=	models.EmailField(default='sin@email.com', null=False, max_length=30)
	#CollaboratorFavoriteKf	= 	models.ForeignKey(tb_collaborator, on_delete=models.CASCADE, null=False, default='')
	#addressClientTwo		= 	models.TextField(default='', null=False)
	#isSendPromotions		=	models.BooleanField()
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	#isVip					= 	models.BooleanField()
	#StatusKf				=	models.ForeignKey(tb_status_turn, on_delete=models.CASCADE, null=False, default='')
	#TypeClienteKf			=	models.ForeignKey(tb_type_client, on_delete=models.CASCADE, null=False, default='')
	def __str__(self):
		return self.user.username
	class Meta:
		managed = True
		db_table = 'egresos' 





