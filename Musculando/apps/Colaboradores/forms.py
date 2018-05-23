from django import forms
from apps.Colaboradores.models import tb_colaboradores
from django.forms import ModelForm, Media,TextInput, NumberInput,EmailInput,URLInput,PasswordInput,FileInput,Textarea,DateInput,DateTimeInput,Select
from django.forms import extras



class ColaboradoresRegisterForm(forms.ModelForm):
	class Meta:
		model = tb_colaboradores
		fields = [
		'honorariosPorHora',
		'diasParaElPremio',
		'tipoColaborador',
		]
		labels = {
		'honorariosPorHora': 'Honorario Por Hora' ,
		'diasParaElPremio': 'Dias Para El Premio',
		'tipoColaborador': 'Tipos de De colaboradores' ,		
		}
		widgets = {
		'honorariosPorHora': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Ingrese El Primer Nombre Del Usuario'}),

		'diasParaElPremio': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Ingrese El Primer Nombre Del Usuario'}),

		'tipoColaborador': Select(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Ingrese El Primer Nombre Del Usuario'}),

		#'descriptionProduct': Textarea(attrs={'class':'form-control', 
		#	'required':True ,
		#	 'autofocus':True,
		#	  'autocomplete':'off',
		#	   ,'placeholder':'Direccion Principal Del Nuevo Proveedor',
		#	   'cols': 2, 
		#	   'rows': 6}),
		}
          
		exclude = ['user',]