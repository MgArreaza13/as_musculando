from datetime import datetime 

def Liquidacion(request):
	hoy = datetime.today().day
	liquidacion = False
	if (hoy == 1):
		####se activa la accion para la liquidacion 
		liquidacion = True
	return {'liquidacion':liquidacion}