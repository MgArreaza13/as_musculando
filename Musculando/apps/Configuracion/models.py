from django.db import models
from django.conf import settings
# Create your models here.

class tb_turn_sesion(models.Model):
	user 					=	models.ForeignKey(settings.AUTH_USER_MODEL)
	nameturnsession			=	models.CharField(default='', null=False, max_length=30,)
	HoraTurn				=	models.TimeField(auto_now=False, auto_now_add=False, blank=False, null=False, default='')
	HoraTurnEnd				=	models.TimeField(auto_now=False, auto_now_add=False, blank=False, null=False, default='')
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	def __str__(self):
		return self.nameturnsession


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

class tb_tipoHorario(models.Model):
	user 					=	models.ForeignKey(settings.AUTH_USER_MODEL)
	nametipoHorario			=	models.CharField(default='', null=False, max_length=30, unique=True)
	HoraTurn				=	models.TimeField(auto_now=False, auto_now_add=False, blank=False, null=False, default='')
	HoraTurnEnd				=	models.TimeField(auto_now=False, auto_now_add=False, blank=False, null=False, default='')
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	def __str__(self):
		return self.nametipoHorario

class tb_porcentaje(models.Model):
	user 							=	models.ForeignKey(settings.AUTH_USER_MODEL)
	porcentaje						=	models.FloatField(default='0', null=True,)
	dateCreate						=	models.DateField(auto_now=True, blank=False)
	descripcion	 			        =	models.TextField(default='Sin Descripcion', null=True, max_length=3000)
	
	
	def __str__(self):
		return self.descripcion
	class Meta:
		managed = True
		db_table = 'porcentaje' 