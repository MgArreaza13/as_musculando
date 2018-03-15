from django.db import models
from django.conf import settings
# Create your models here.



class tb_plan(models.Model):
	user 					=	models.ForeignKey(settings.AUTH_USER_MODEL)
	nombrePlan				=	models.CharField(default='Sin Nonbre', null=True, max_length=30)
	precioPlan				=	models.CharField(default='000000', null=True, max_length=30)
	descripcionPlan			=	models.TextField(default='Sin Datos', null=True)
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	def __str__(self):
		return self.nombrePlan
	class Meta:
		managed = True
		db_table = 'planes'