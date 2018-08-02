from django import forms
from apps.Colaboradores.models import tb_colaboradores
from django.forms import ModelForm, Media,TextInput, NumberInput,CheckboxInput,EmailInput,URLInput,PasswordInput,FileInput,Textarea,DateInput,DateTimeInput,Select
from django.forms import extras



class ColaboradoresRegisterForm(forms.ModelForm):
	class Meta:
		model = tb_colaboradores
		fields = [
		'tipoColaborador',
		'honorariosMensuales',
		'montoXClase',
		'comisionXClase',
		'presentimo',
		'montoAguinaldo',
		'isHonorarios',
		'isMontoXClase',
		'isComison',
		'isPresentimo',
		'isAguinaldo',



		]
		labels = {
		'tipoColaborador': 'Seleccione El tipo De Colaborador',
		'honorariosMensuales': 'Abono Mensual',
		'montoXClase': 'Monto Fijo Por Clase',
		'comisionXClase': 'Comision Por Clase',
		'presentimo': 'Presentimo',
		'montoAguinaldo': 'Aguinaldo',
		'isHonorarios' : 'Abono Mensual?',
		'isMontoXClase': 'Monto Por Clase?',
		'isComison': 'Comision Por Clase?',
		'isPresentimo': 'Presentimo?',
		'isAguinaldo' : 'Aguinaldo?',		
		
		}
		widgets = {
		'tipoColaborador': Select(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Ingrese El Primer Nombre Del Usuario'}),

		'honorariosMensuales': NumberInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Ingrese El Honorario Mensual , Sino Posee Dejar en Cero'}),

		'montoXClase': NumberInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Ingrese El Monto Fijo Por clase , Sino Posee Dejar en Cero'}),

		'comisionXClase': NumberInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Ingrese la comision Por clase , Sino Posee Dejar en Cero'}),

		'presentimo': NumberInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Ingrese el presentimo , Sino Posee Dejar en Cero'}),

		'montoAguinaldo': NumberInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Ingrese Aguinaldo , Sino Posee Dejar en Cero'}),

		


		#'descriptionProduct': Textarea(attrs={'class':'form-control', 
		#	'required':True ,
		#	 'autofocus':True,
		#	  'autocomplete':'off',
		#	   ,'placeholder':'Direccion Principal Del Nuevo Proveedor',
		#	   'cols': 2, 
		#	   'rows': 6}),
		}
          
		exclude = ['user','dateCreate', 'cuentaColaborador', 'isPresentimoPay', 'isHonorariosUpload']