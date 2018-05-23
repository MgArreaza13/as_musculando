from django import forms
from apps.Caja.models import tb_egreso
from django.forms import ModelForm, Media,TextInput, NumberInput,EmailInput,URLInput,PasswordInput,FileInput,Textarea,DateInput,DateTimeInput,Select
from django.forms import extras



class EgresoRegisterForm(forms.ModelForm):
	class Meta:
		model = tb_egreso
		fields = [
		'monto',
		'descripcion',
		'proveedor',
		'tipoDeEgreso',
		]
		labels = {
			'monto':'Monto de Egreso',
			'descripcion' :'Descripcion del Egreso',
			'proveedor' :'Proveedor',
			'tipoDeEgreso' :'Tipo de Egreso',	
		}
		widgets = {
		'monto': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Monto de Egreso'}),

		'descripcion': Textarea(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Descripcion del Egreso'}),

		'proveedor': Select(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Proveedor'}),

		'tipoDeEgreso': Select(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Tipo de Egreso'}),

		#'descriptionProduct': Textarea(attrs={'class':'form-control', 
		#	'required':True ,
		#	 'autofocus':True,
		#	  'autocomplete':'off',
		#	   ,'placeholder':'Direccion Principal Del Nuevo Proveedor',
		#	   'cols': 2, 
		#	   'rows': 6}),
		}
          
		exclude = ['user',]