from apps.UserProfile.models import tb_profile
from apps.Socios.models import tb_socio
from django.contrib.auth import logout as logout_django
from django.shortcuts import redirect

##############RETORNO DE PERFIL############### 
def ProfileContextProcesor(request):
	response = {}
	perfil = tb_profile.objects.filter(user__id = request.user.id)
	if len(perfil) == 0:
		response = {
		'perfil':'Null',
		'is_complete':'False'
		}
	else:
		response = {
		'perfil':perfil[0],
		'is_complete':perfil[0].is_complete
		}
	return {'profile_response':response}




###############RETORNO DE STATUS DE SOCIO#####################
def SocioContextProcesor(request):
	####Validacion####
	response = {}
	if request.user.id != None:
		
		perfil =  tb_profile.objects.filter(user__id = request.user.id )
		print(perfil)
		if len(perfil) == 0 :
			#####No tiene perfil por lo que deslogueo y retorno al inicio
			logout_django(request)
			return redirect('Panel:Login')
		else:
			#### tiene perfil ###
			perfil_user = perfil[0]
			if perfil_user.tipoUser == 'Socio':
				#####Es Socio#####
				socio = tb_socio.objects.get(perfil__id = perfil_user.id )
				response = {
					'status': socio.status,
				}
			else:
				####No Es Socio######
				response = {
				'status':'False'
				}
	else:
				####No Es Socio######
		response = {
		'status':'False'
		}
	return {'socio_profile':response}












def QueryUser(id):
	query_user = tb_profile.objects.filter(user__id = id)
	if len(query_user) == 0 :
		perfil = False
	else:
		perfil = True
	return perfil