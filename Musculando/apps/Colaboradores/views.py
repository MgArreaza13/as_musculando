from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
#####################MODELOS##########################
from apps.Colaboradores.models import tb_colaboradores
from apps.UserProfile.models import tb_profile
from apps.Configuracion.models import tb_tipoColaborador
#####################FORMS#############################
from apps.Colaboradores.forms import ColaboradoresRegisterForm
from apps.UserProfile.forms import ProfileForm
#####################TAREAS############################
from apps.tasks.Email_tasks import ColaboradorEliminado
# Create your views here.


def ListaDeColaboradores(request):
	Colaboradores = tb_colaboradores.objects.all()
	contexto = {
		'Colaboradores':Colaboradores
	}
	return render(request, 'Colaboradores/lista.html', contexto)




#def EliminarColaborador(request):
#	status = None
#	id_colaborador = request.GET.get('id', None)
#	queryset = tb_colaboradores.objects.get(id = id_colaborador)
#	ColaboradorEliminado.delay()
#	queryset.delete()
#	status = 200
#	return HttpResponse(status)
#
#
#
#
#
def NewColaborador(request):
	Form = ProfileForm()
	Form2 = ColaboradoresRegisterForm()
	fallido = None
	if request.method == 'POST':
		
		#Form  = UsuarioForm(request.POST, request.FILES  or None)
		Form = ProfileForm(request.POST, request.FILES  or None)
		Form2 = ColaboradoresRegisterForm(request.POST, request.FILES  or None)
		if Form.is_valid() and Form2.is_valid():
			nuevoPerfil = tb_profile()
			#nuevoPerfil.user = 
			nuevoPerfil.nameUser = request.POST['nameUser']
			nuevoPerfil.dni = request.POST['dni']
			nuevoPerfil.mailUser = request.POST['mailUser']
			nuevoPerfil.tipoUser = 'Colaborador'
			if len(request.FILES) != 0:
				nuevoPerfil.image = request.FILES['ImagenDePerfil']
			else:
				nuevoPerfil.image = 'Null'
			nuevoPerfil.save()
			nuevoColaborador = Form2.save(commit=False)
			nuevoColaborador.user = tb_profile.objects.get(id = nuevoPerfil.id)
			#nuevoColaborador.honorariosPorHora =  request.POST['honorariosPorHora']
			#nuevoColaborador.diasParaElPremio =  request.POST['diasParaElPremio']
			#nuevoColaborador.tipoColaborador =  tb_tipoColaborador.objects.get(id =request.POST['tipoColaborador'])
			nuevoColaborador.save() 
				################ENVIAR CORREO QUE SE CREO EL PERFIL DE SOCIO CORRECTAMENTE ########
			#NewSocioMAil.delay(request.POST['nameUser'], nuevoSocio.TarifaMensual.precioPlan, nuevoSocio.TarifaMensual.nombrePlan, request.POST['mailUser'])
			return redirect('Colaboradores:ListaDeColaboradores')
		else:
			#Form	= UsuarioForm(request.POST , request.FILES  or None)
			Form	= ProfileForm(request.POST, request.FILES  or None)
			Form2 = ColaboradoresRegisterForm(request.POST, request.FILES  or None)
			fallido = "No pudimos guardar sus datos, intentalo de nuevo luego de verificarlos" 
	contexto = {
	'Form':Form,
	'Form2':Form2,
	'fallido':fallido,
	}
	return render(request, 'Colaboradores/nuevo.html' , contexto)
#
#
#
#
#
#def UpdateColaboradores(request, id_colaborador):
#	colaborador= tb_colaboradores.objects.get(id=id_colaborador)
#	perfil = tb_profile.objects.get(id = colaborador.user.id)
#	fallido = None
#	if request.method == 'GET':
#		Form= ProfileForm(instance = perfil)
#		Form2 = ColaboradoresRegisterForm(instance = colaborador)
#	else:
#		Form = ProfileForm(request.POST , request.FILES  ,  instance = perfil)
#		Form2 = ColaboradoresRegisterForm(request.POST , request.FILES  ,  instance = colaborador)
#		if Form.is_valid() and Form2.is_valid():
#			nuevoPerfil = Form.save(commit=False)
#			#nuevoPerfil.user = 
#			nuevoPerfil.nameUser = request.POST['nameUser']
#			nuevoPerfil.dni = request.POST['dni']
#			nuevoPerfil.mailUser = request.POST['mailUser']
#			nuevoPerfil.tipoUser = 'Colaborador'
#			if len(request.FILES) != 0:
#				nuevoPerfil.image = request.FILES['ImagenDePerfil']
#			else:
#				nuevoPerfil.image = 'Null'
#			nuevoPerfil.save()
#			nuevoColaborador = Form2.save(commit=False)
#			#nuevoColaborador.user = tb_profile.objects.get(id = nuevoPerfil.id)
#			nuevoColaborador.honorariosPorHora =  request.POST['honorariosPorHora']
#			nuevoColaborador.diasParaElPremio =  request.POST['diasParaElPremio']
#			nuevoColaborador.tipoColaborador =  tb_tipoColaborador.objects.get(id =request.POST['tipoColaborador'])
#			nuevoColaborador.save() 
#				################ENVIAR CORREO QUE SE CREO EL PERFIL DE SOCIO CORRECTAMENTE ########
#			#NewSocioMAil.delay(request.POST['nameUser'], nuevoSocio.TarifaMensual.precioPlan, nuevoSocio.TarifaMensual.nombrePlan, request.POST['mailUser'])
#			return redirect('Colaboradores:ListaDeColaboradores')
#		else:
#			#Form	= UsuarioForm(request.POST , request.FILES  or None)
#			Form	= ProfileForm(request.POST, request.FILES  or None)
#			Form2 = ColaboradoresRegisterForm(request.POST, request.FILES  or None)
#			fallido = "No pudimos guardar sus datos, intentalo de nuevo luego de verificarlos" 
#	return render (request, 'Colaboradores/nuevo.html' , {'Form':Form,'Form2':Form2,'fallido':fallido,})