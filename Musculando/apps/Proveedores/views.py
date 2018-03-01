from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

#############MODELOS#########################
from apps.Proveedores.models import tb_proveedor




# Create your views here.

#############NuevoProveedorAjax################
def NuevoProveedor(request):
	status = 200
	is_proveedor = False #Proveedor No existe
	Nombre = request.GET.get('Nombre', None)
	Correo = request.GET.get('Correo', None)
	RazonSocial = request.GET.get('RazonSocial', None)
	Telefono = request.GET.get('Telefono', None)
	Direccion = request.GET.get('Direccion', None)
	proveedores = tb_proveedor.objects.all()
	for i in range(0,len(proveedores)):
		if(proveedores[i].nameProveedor == Nombre and proveedores[i].email == Correo):
			#existe el proveedor
			is_proveedor = True
	if is_proveedor == False: #No existe el proveedor
		#Creo el Proveedor
		NuevoProveedor = tb_proveedor()
		NuevoProveedor.nameProveedor = Nombre
		NuevoProveedor.email = Correo
		if RazonSocial == '':
			NuevoProveedor.razonSocial = 'Sin Datos'
		else:
			NuevoProveedor.razonSocial = RazonSocial
		if Telefono == '':
			NuevoProveedor.phoneNumberProveedor = '+00000000'
		else:
			NuevoProveedor.phoneNumberProveedor = Telefono
		if Direccion == '':
			NuevoProveedor.addressProveedor = 'Sin Datos'
		else:
			NuevoProveedor.addressProveedor = Direccion
		NuevoProveedor.save()
	else:
		status = 405
	return HttpResponse(status)

@login_required(login_url = 'Panel:Login' )
def Nuevo(request):
	return render(request,'Proveedores/Nuevo.html', )

@login_required(login_url = 'Panel:Login' )
def ListaDeProveedores(request):
	proveedores = tb_proveedor.objects.all()
	contexto = {
		'proveedores':proveedores,
	}
	return render(request,'Proveedores/ListaDeProveedores.html', contexto)