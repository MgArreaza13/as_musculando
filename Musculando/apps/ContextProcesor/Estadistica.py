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

	if len(TotalIngresos) == 0 or len(TotalEgresos) == 0 :
		balanceGeneral = 0
	elif  TotalIngresos['total'] != None and TotalEgresos['total']!=None:
		balanceGeneral = TotalIngresos['total'] - TotalEgresos['total']
	else :
		balanceGeneral = 0
	#print(balanceGeneral)

	if len(totalIngrsos_mensual) == 0 or len(totalEgresos_mensual) == 0:
		balanceGeneralMensual = 0
	elif totalIngrsos_mensual['total_mensual'] != None and totalEgresos_mensual['total_mensual'] != None:
		balanceGeneralMensual = float(totalIngrsos_mensual['total_mensual']) - float(totalEgresos_mensual['total_mensual'])
	else:
		balanceGeneralMensual = 0
	return {'totalIngresos':TotalIngresos, 'totalIngrsos_mensual':totalIngrsos_mensual, 'TotalEgresos':TotalEgresos, 'totalEgresos_mensual':totalEgresos_mensual, 'balanceGeneral':balanceGeneral, 'balanceGeneralMensual':balanceGeneralMensual }



def ResumenSociosActivos(request):
	queryset = tb_socio.objects.filter(status = 'Activo')
	totalSociosActivos = len(queryset)
	return {'totalSociosActivos':totalSociosActivos}



def ResumenPlanes(request):
	queryset = tb_plan.objects.all()
	totalPlanes = len(queryset)
	return {'totalPlanes':totalPlanes}