from apps.UserProfile.models import tb_profile
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
	print(response)
	return {'profile_response':response}



def QueryUser(id):
	query_user = tb_profile.objects.filter(user__id = id)
	if len(query_user) == 0 :
		perfil = False
	else:
		perfil = True
	return perfil