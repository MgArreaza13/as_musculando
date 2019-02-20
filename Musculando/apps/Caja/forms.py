from django import forms
from apps.Caja.models import tb_egreso
from apps.Caja.models import tb_ingresos
from django.forms import ModelForm, Media,TextInput, NumberInput,EmailInput,URLInput,PasswordInput,FileInput,Textarea,DateInput,DateTimeInput,Select
from django.forms import extras





class IngresoRegisterForm(forms.ModelForm):
	class Meta:
		model = tb_ingresos
		fields = [
		'monto',
		'descripcion',
		'tipoDeIngresos',
		'tipoPago',
		]
		labels = {
			'monto':'Monto de Ingreso',
			'descripcion' :'Descripcion del Ingreso',
			'tipoDeIngresos' :'Tipo de Ingreso',
			'tipoPago' :'Forma de Pago',
			
		}
		widgets = {
		'monto': NumberInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Monto de Ingreso'}),

		'descripcion': Textarea(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Descripcion del Ingreso'}),

		

		'tipoDeIngresos': Select(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Tipo de Ingreso'}),

		'tipoPago': Select(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Forma de Pago'}),

		#'descriptionProduct': Textarea(attrs={'class':'form-control', 
		#	'required':True ,
		#	 'autofocus':True,
		#	  'autocomplete':'off',
		#	   ,'placeholder':'Direccion Principal Del Nuevo Proveedor',
		#	   'cols': 2, 
		#	   'rows': 6}),
		}
          
		exclude = ['user', 'dateCreate']






class EgresoRegisterForm(forms.ModelForm):
	class Meta:
		model = tb_egreso
		fields = [
		'monto',
		'descripcion',
		'tipoDeEgreso',
		'proveedor',
		'colaborador',
		'tipoPago',
		]
		labels = {
			'monto':'Monto de Egreso',
			'descripcion' :'Descripcion del Egreso',
			'proveedor' :'Proveedor',
			'tipoDeEgreso' :'Tipo de Egreso',
			'colaborador': 'Colaborador',
			'tipoPago': 'Forma de Pago',

		}
		widgets = {
		'monto': NumberInput(attrs={'class':'form-control', 
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
			  'required':False,
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Proveedor'}),
		'colaborador': Select(attrs={'class':'form-control', 
			  'required':False,
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Colaborador'}),

		'tipoDeEgreso': Select(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Tipo de Egreso'}),

		'tipoPago': Select(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Forma de Pago'}),

		#'descriptionProduct': Textarea(attrs={'class':'form-control', 
		#	'required':True ,
		#	 'autofocus':True,
		#	  'autocomplete':'off',
		#	   ,'placeholder':'Direccion Principal Del Nuevo Proveedor',
		#	   'cols': 2, 
		#	   'rows': 6}),
		}
          
		exclude = ['user', 'colaborador', 'proveedor']