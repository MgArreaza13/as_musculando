##########################MODELOS#######################
from apps.Caja.models import tb_ingreso_mensualidad
from apps.Caja.models import tb_egreso
from apps.Caja.models import tb_ingresos

from apps.Socios.models import tb_socio
from apps.Configuracion.models import tb_plan
from apps.UserProfile.models import tb_profile
##########################otros import ######################
from datetime import date 
from django.db.models import Count, Min, Sum, Avg


def ResumenIngresos(request):
	#ingreso y egreso diario 
	ingresos_mensualidad_hoy = tb_ingreso_mensualidad.objects.filter(dateCreate = date.today()).aggregate(total=Sum('monto'))
	ingresos_hoy = tb_ingresos.objects.filter(dateCreate= date.today()).aggregate(total=Sum('monto'))
	if ingresos_mensualidad_hoy['total'] == None:
		ingresos_mensualidad_hoy['total'] = 0
	if ingresos_hoy['total'] == None:
		ingresos_hoy['total'] = 0
	TotalIngresosHoy = ingresos_mensualidad_hoy['total'] + ingresos_hoy['total']

	totalEgresosHoy =  tb_egreso.objects.filter(dateCreate = date.today()).aggregate(total=Sum('monto'))

	if totalEgresosHoy['total']==None:
		balanceGeneralHoy = TotalIngresosHoy
	elif  totalEgresosHoy['total']!=None:
		balanceGeneralHoy = TotalIngresosHoy - totalEgresosHoy['total']
	else :
		balanceGeneralHoy = 0




	#Total ingresos 
	ingresos_socios 	= tb_ingreso_mensualidad.objects.all().aggregate(total=Sum('monto'))
	ingresos_especial 	= tb_ingresos.objects.all().aggregate(total=Sum('monto'))
	if ingresos_socios['total'] == None:
		ingresos_socios['total'] = 0
	if ingresos_especial['total'] == None:
		ingresos_especial['total'] = 0
	TotalIngresos = ingresos_socios['total'] + ingresos_especial['total']



	
	# ingresos mensual 
	ingreso_mensual_socio 		=	tb_ingreso_mensualidad.objects.filter(dateCreate__year = date.today().year ).filter(dateCreate__month = date.today().month).aggregate(total_mensual=Sum('monto'))
	ingreso_mensual 			=	tb_ingresos.objects.filter(dateCreate__year = date.today().year ).filter(dateCreate__month = date.today().month).aggregate(total_mensual=Sum('monto'))
	if ingreso_mensual_socio['total_mensual'] == None:
		ingreso_mensual_socio['total_mensual'] = 0
	if ingreso_mensual ['total_mensual'] == None:
		ingreso_mensual ['total_mensual'] = 0

	totalIngrsos_mensual = float(ingreso_mensual_socio['total_mensual']) + float(ingreso_mensual['total_mensual'])
	


	#Total Egresos
	TotalEgresos = tb_egreso.objects.all().aggregate(total=Sum('monto'))
	#Egresos Mensual 
	totalEgresos_mensual = tb_egreso.objects.filter(dateCreate__year = date.today().year ).filter(dateCreate__month = date.today().month).aggregate(total_mensual=Sum('monto'))

	if len(TotalEgresos) == 0 :
		balanceGeneral = TotalIngresos
	elif  TotalEgresos['total']!=None:
		balanceGeneral = TotalIngresos - TotalEgresos['total']
	else :
		balanceGeneral = 0
	#print(balanceGeneral)

	if  totalEgresos_mensual['total_mensual'] == None:
		balanceGeneralMensual = totalIngrsos_mensual
	elif totalEgresos_mensual['total_mensual'] != None:
		balanceGeneralMensual = totalIngrsos_mensual - totalEgresos_mensual['total_mensual']
	else:
		balanceGeneralMensual = 0
	return {'totalIngresos':TotalIngresos, 
			'totalIngrsos_mensual':totalIngrsos_mensual, 
			'TotalEgresos':TotalEgresos, 
			'totalEgresos_mensual':totalEgresos_mensual, 
			'balanceGeneral':balanceGeneral, 
			'balanceGeneralMensual':balanceGeneralMensual, 
			'TotalIngresosHoy':TotalIngresosHoy,
			'totalEgresosHoy':totalEgresosHoy,
			'balanceGeneralHoy':balanceGeneralHoy }



def ResumenSociosActivos(request):
	queryset = tb_socio.objects.filter(status = 'Activo')
	totalSociosActivos = len(queryset)
	return {'totalSociosActivos':totalSociosActivos}



def ResumenPlanes(request):
	queryset = tb_plan.objects.all()
	totalPlanes = len(queryset)
	return {'totalPlanes':totalPlanes}