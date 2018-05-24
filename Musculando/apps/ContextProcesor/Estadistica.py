##########################MODELOS#######################
from apps.Caja.models import tb_ingreso_mensualidad
from apps.Caja.models import tb_egreso
from apps.Socios.models import tb_socio
from apps.Configuracion.models import tb_plan
from apps.UserProfile.models import tb_profile
##########################otros import ######################
from datetime import date 
from django.db.models import Count, Min, Sum, Avg


def ResumenIngresos(request):
	#Total ingresos 
	TotalIngresos = tb_ingreso_mensualidad.objects.all().aggregate(total=Sum('monto'))
	# ingresos mensual 
	
	totalIngrsos_mensual = tb_ingreso_mensualidad.objects.filter(dateCreate__month = date.today().month).aggregate(total_mensual=Sum('monto'))
	
	#Total Egresos
	TotalEgresos = tb_egreso.objects.all().aggregate(total=Sum('monto'))
	#Egresos Mensual 
	totalEgresos_mensual = tb_egreso.objects.filter(dateCreate__month = date.today().month).aggregate(total_mensual=Sum('monto'))

	balanceGeneral = TotalIngresos['total'] - TotalEgresos['total']
	#print(balanceGeneral)

	balanceGeneralMensual = totalIngrsos_mensual['total_mensual'] - totalEgresos_mensual['total_mensual']
	
	return {'totalIngresos':TotalIngresos, 'totalIngrsos_mensual':totalIngrsos_mensual, 'TotalEgresos':TotalEgresos, 'totalEgresos_mensual':totalEgresos_mensual, 'balanceGeneral':balanceGeneral, 'balanceGeneralMensual':balanceGeneralMensual }



def ResumenSociosActivos(request):
	queryset = tb_socio.objects.filter(status = 'Activo')
	totalSociosActivos = len(queryset)
	return {'totalSociosActivos':totalSociosActivos}



def ResumenPlanes(request):
	queryset = tb_plan.objects.all()
	totalPlanes = len(queryset)
	return {'totalPlanes':totalPlanes}