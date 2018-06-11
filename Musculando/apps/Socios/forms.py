from django import forms
from apps.Socios.models import tb_socio
from django.forms import ModelForm, Media,TextInput, NumberInput,EmailInput,URLInput,PasswordInput,FileInput,Textarea,DateInput,DateTimeInput,Select
    
from django.forms import extras
class SociosRegisterForm(forms.ModelForm):
	class Meta:
		model = tb_socio
		fields = [
		'obraSocial',
		'dateInactive_socio'

		]
		labels = {
		'obraSocial':'Obra Social',	
		'dateInactive_socio':'Fecha de Desactivacion De Socio'	
		}
		widgets = {
		'obraSocial': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':True,
			  'autocomplete':'off',
			   'placeholder':'Ingrese El Primer Nombre Del Usuario'}),

		'dateInactive_socio': DateInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':True,
			  'autocomplete':'off',
			  'type':'date',
			  'placeholder':'Fecha de Inicio'}),

		#'descriptionProduct': Textarea(attrs={'class':'form-control', 
		#	'required':True ,
		#	 'autofocus':True,
		#	  'autocomplete':'off',
		#	   ,'placeholder':'Direccion Principal Del Nuevo Proveedor',
		#	   'cols': 2, 
		#	   'rows': 6}),
		}
          
		exclude = ['perfil', 'status', 'dateCreate_socio', 'TarifaMensual']
