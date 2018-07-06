from datetime import datetime 

def presentimo(request):
	hoy = datetime.today().day
	presentimo = False
	if (hoy == 1):
		####se activa la accion para la presentimo 
		presentimo = True
	return {'presentimo':presentimo}