from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Media,TextInput, NumberInput,EmailInput,URLInput,PasswordInput,FileInput,Textarea,DateInput,DateTimeInput,Select
from django.forms import extras
#######################MODELOS####################
from apps.Configuracion.models import tb_plan
from apps.Configuracion.models import tb_turn_sesion
from apps.Configuracion.models import tb_porcentaje

class PlanRegisterForm(forms.ModelForm):
	class Meta:
		model = tb_plan
		fields = [
		'nombrePlan',
		'precioPlan',
		'precioPlanAnual',
		'descripcionPlan',
		
		]
		labels = {
		'nombrePlan':'Nombre Plan',
		'precioPlan':'Precio Plan',
		'precioPlanAnual':'Precio De Oferta Anual',
		'descripcionPlan': 'Decripcion',
		}
		widgets = {
		'nombrePlan': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  
			  'autocomplete':'off',
			   'placeholder':'Ingrese Nombre Del Plan'}),

		'precioPlan': NumberInput(attrs={'class':'form-control', 
			  'required':'False',
			  
			  'autocomplete':'off',
			   'placeholder':'Precio del Plan'}),

		'precioPlanAnual': NumberInput(attrs={'class':'form-control', 
			  'required':'False',
			  
			  'autocomplete':'off',
			   'placeholder':'Promocion Anual'}),

		'descripcionPlan': Textarea(attrs={'class':'form-control', 
			  'required':'False',
			  'value':'Sin Descripcion',
			  'autocomplete':'off',
			   'placeholder':'Descripcion'}),

		#'descriptionProduct': Textarea(attrs={'class':'form-control', 
		#	'required':True ,
		#	 'autofocus':True,
		#	  'autocomplete':'off',
		#	   ,'placeholder':'Direccion Principal Del Nuevo Proveedor',
		#	   'cols': 2, 
		#	   'rows': 6}),
		}
          
		exclude = ['user',  'dateCreate',]

class tipoTurnForm(forms.ModelForm):
	
	class Meta:
		model = tb_turn_sesion
		fields = [
		'nameturnsession',
		]
		exclude = ['user','dateCreate', 'HoraTurn' , 'dateCreate' ]
		labels = {
		'nametipoTurno':'Descripcion', 		
		}
		widgets = {
		}

class PorcentajeRegisterForm(forms.ModelForm):
	class Meta:
		model = tb_porcentaje
		fields = [
		'porcentaje',
		'dateCreate',
		'titulo',
		'descripcion',
		'user',
		]
		labels = {
		'porcentaje':'Porcentaje',
		'titulo':'Titulo',
		'descripcion': 'Decripcion',
		}
		widgets = {
		'user': Select(attrs={'class':'form-control', 
			  'required':'False',
			  'value':'Sin Descripcion',
			  'autocomplete':'off',
			   'placeholder':'Usuario'}),

		'porcentaje':  NumberInput(attrs={'class':'form-control', 
			  'required':'True',
			  
			  'autocomplete':'off',
			   'placeholder':'Porcentaje'}),

				
		'titulo': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'value':'Sin Descripcion',
			  'autocomplete':'off',
			   'placeholder':'Titulo'}),
		

		'descripcion': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'value':'Sin Descripcion',
			  'autocomplete':'off',
			   'placeholder':'Descripcion'}),

		#'descriptionProduct': Textarea(attrs={'class':'form-control', 
		#	'required':True ,
		#	 'autofocus':True,
		#	  'autocomplete':'off',
		#	   ,'placeholder':'Direccion Principal Del Nuevo Proveedor',
		#	   'cols': 2, 
		#	   'rows': 6}),
		}
          
		exclude = ['dateCreate','user','titulo',]