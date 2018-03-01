from django.db import models

# Create your models here.


class tb_clase (models.Model):
	nameClass					=	models.CharField(default='Sin Datos', null=True, max_length=30)
	#Dias						=	models.CharField(default='abc-123', null=True, max_length=30)
	#Horarios					=	models.CharField(default='+000000000', null=True, max_length=30)
	#Profesores 					= 	models.EmailField(default='sin@datos.com', null=True, max_length=30)
	#precio_socios 				=	models.TextField(default='Sin Datos', null=True)
	#porcentaje_profesor			=	models.DateField(auto_now=True, blank=False)
	#user 						=	models.ForeignKey(settings.AUTH_USER_MODEL)
	#cuit						=	models.IntegerField(default='', null=True)
	#phoneNumberProveedorTwo		=	models.CharField(default='', null=True, max_length=30)
	#personaACargo				=	models.CharField(default='', null=True, max_length=30)
	#paginaWeb 					=	models.URLField(default='', null=True,max_length=3000)
	#urlPhoto					=   models.URLField(default='', null=True,max_length=3000)
	#CollaboratorFavoriteKf		= 	models.ForeignKey(tb_collaborator, on_delete=models.CASCADE, null=False, default='')
	#addressProveedorTwo			= 	models.TextField(default='', null=False)
	#isSendPromotions			=	models.BooleanField()
	#isVip						= 	models.BooleanField()
	#StatusKf					=	models.ForeignKey(tb_status_turn, on_delete=models.CASCADE, null=False, default='')
	#TypeClienteKf				=	models.ForeignKey(tb_type_client, on_delete=models.CASCADE, null=False, default='')
	def __str__(self):
		return self.nameClass
	class Meta:
		managed = True
		db_table = 'clases'