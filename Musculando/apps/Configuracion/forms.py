from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Media,TextInput, NumberInput,EmailInput,URLInput,PasswordInput,FileInput,Textarea,DateInput,DateTimeInput,Select
from django.forms import extras
#######################MODELOS####################
from apps.Configuracion.models import tb_plan

class PlanRegisterForm(forms.ModelForm):
	class Meta:
		model = tb_plan
		fields = [
		'nombrePlan',
		'precioPlan',
		'descripcionPlan',
		
		]
		labels = {
		'nombrePlan':'Nombre Plan',
		'precioPlan':'Precio Plan',
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
