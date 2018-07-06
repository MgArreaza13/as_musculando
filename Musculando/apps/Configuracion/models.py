from django.db import models
from django.conf import settings
# Create your models here.



class tb_plan(models.Model):
	user 							=	models.ForeignKey(settings.AUTH_USER_MODEL)
	nombrePlan						=	models.CharField(default='Sin Nonbre', null=True, max_length=30)
	precioPlan 						=	models.CharField(default='000000', null=True, max_length=30)
	precioPlanAnual					=	models.CharField(default='000000', null=True, max_length=30)
	descripcionPlan					=	models.TextField(default='Sin Datos', null=True)
	dateCreate						=	models.DateField(auto_now=True, blank=False)
	def __str__(self):
		return self.nombrePlan
	class Meta:
		managed = True
		db_table = 'planes'


class tb_formasDePago(models.Model):
	user 					=	models.ForeignKey(settings.AUTH_USER_MODEL)
	nameFormasDePago		=	models.CharField(default='Sin Datos', null=False, max_length=30, unique=True)
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	def __str__(self):
		return self.nameFormasDePago
	class Meta:
		managed = True
		db_table = 'formas_de_pago'	


class tb_tipoColaborador(models.Model):
	user 					=	models.ForeignKey(settings.AUTH_USER_MODEL)
	tipodeColaborador		=	models.CharField(default='Sin Datos', null=False, max_length=30, unique=True)
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	def __str__(self):
		return self.tipodeColaborador
	class Meta:
		managed = True
		db_table = 'tipo_de_colaborador'	



class tb_tipoEgreso(models.Model):
	user 					=	models.ForeignKey(settings.AUTH_USER_MODEL)
	tipodeEgreso			=	models.CharField(default='Sin Datos', null=False, max_length=30, unique=True)
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	def __str__(self):
		return self.tipodeEgreso
	class Meta:
		managed = True
		db_table = 'tipo_de_egreso'



class tb_tipoIngreso(models.Model):
	user 					=	models.ForeignKey(settings.AUTH_USER_MODEL)
	tipodeIngreso			=	models.CharField(default='Sin Datos', null=False, max_length=30, unique=True)
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	def __str__(self):
		return self.tipodeIngreso
	class Meta:
		managed = True
		db_table = 'tipo_de_ingreso'