from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Media,TextInput, NumberInput,EmailInput,URLInput,PasswordInput,FileInput,Textarea,DateInput,DateTimeInput,Select
from django.forms import extras
#######################MODELOS####################
from apps.Configuracion.models import tb_plan
from apps.Configuracion.models import tb_turn_sesion
from apps.Configuracion.models import tb_porcentaje
from apps.Configuracion.models import tb_mailsAdministrador
from apps.Configuracion.models import tb_termino

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
		
		'descripcion',
		'user',
		]
		labels = {
		'porcentaje':'Porcentaje',
		
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
          
		exclude = ['dateCreate','user',]

class EmailRegisterForm(forms.ModelForm):
	class Meta:
		model = tb_mailsAdministrador
		fields = [
		'mail',
		'dateCreate',
		'user',
		]
		labels = {
		'mail':'Email',
		
		}
		widgets = {
		
		'mail': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'value':'Sin Descripcion',
			  'autocomplete':'off',
			   'placeholder':'Email'}),

		#'descriptionProduct': Textarea(attrs={'class':'form-control', 
		#	'required':True ,
		#	 'autofocus':True,
		#	  'autocomplete':'off',
		#	   ,'placeholder':'Direccion Principal Del Nuevo Proveedor',
		#	   'cols': 2, 
		#	   'rows': 6}),
		}
          
		exclude = ['dateCreate','user']


class TerminoRegisterForm(forms.ModelForm):
	class Meta:
		model = tb_termino
		fields = [
		'nameTerminos',
		'descripcion',
		'dateCreate',
		'user',
		]
		labels = {
		'nameTerminos':'Titulo',
		
		}
		widgets = {
		
		'nameTerminos': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'value':'Sin Descripcion',
			  'autocomplete':'off',
			   'placeholder':'Titulo del Termino o Servicio'}),

		'descripcion': Textarea(attrs={'class':'form-control', 
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
          
		exclude = ['dateCreate','user']