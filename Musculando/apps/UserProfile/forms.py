from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.UserProfile.models import tb_profile
from django.forms import ModelForm, Media,TextInput, NumberInput,EmailInput,URLInput,PasswordInput,FileInput,Textarea,DateInput,DateTimeInput,Select
    
from django.forms import extras

class UsuarioForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username',]
		exclude = ['email',]




class ProfileRegisterForm(forms.ModelForm):
	class Meta:
		model = tb_profile
		fields = [
		'nameUser',
		'dni',
		'mailUser',
		'tipoUser',
		
		]
		labels = {
		'nameUser':'Primer Nombre',
		'lastName':'Apellidos',
		'dni': 'Documento De Identidad',
		'movilTlf':'Numero Movil de Contacto',
		'houseTlf': 'Numero Secundario',
		'mailUser':'Correo Electronico',
		'image':'Imagen de Perfil',
		'birthdayDate':'Fecha de Nacimiento',
		'tipoUser':'Seleccione el tipo de Usuario',


		
		}
		widgets = {
		'nameUser': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':True,
			  'autocomplete':'off',
			   'placeholder':'Ingrese El Primer Nombre Del Usuario'}),

		'lastName': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':True,
			  'autocomplete':'off',
			   'placeholder':'Ingrese El Apellido Del Usuario'}),

		'dni': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':True,
			  'autocomplete':'off',
			   'placeholder':'Ingrese El Documento De Identidad Del usuario'}),

		'movilTlf': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':True,
			  'autocomplete':'off',
			   'placeholder':'Ingrese El Numero de Contacto'}),

		'houseTlf': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':True,
			  'autocomplete':'off',
			   'placeholder':'Ingrese un numero de contacto alterno'}),

		'mailUser': EmailInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':True,
			  'autocomplete':'off',
			   'placeholder':'Ingrese su correo electronico de contacto'}),
		'image': FileInput(attrs={'class':'', 
			  'required':'False',
			  'disabled':True,
			  'autocomplete':'off',
			   'placeholder':'Ingrese su imagen de perfil'}),
		'birthdayDate': DateTimeInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':True,
			  'autocomplete':'off',
			   'placeholder':'ingree Su fecha de nacimiento'}),
		'tipoUser': Select(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':True,
			  'autocomplete':'off',
			   'placeholder':'Ingrese su imagen de perfil'}),
		#'descriptionProduct': Textarea(attrs={'class':'form-control', 
		#	'required':True ,
		#	 'autofocus':True,
		#	  'autocomplete':'off',
		#	   ,'placeholder':'Direccion Principal Del Nuevo Proveedor',
		#	   'cols': 2, 
		#	   'rows': 6}),
		}
          
		exclude = ['user',  'dateCreate','movilTlf' ,'is_complete', 'image', 'birthdayDate','lastName',]

class ProfileForm(forms.ModelForm):
	class Meta:
		model = tb_profile
		fields = [
		'nameUser',
		'lastName',
		'dni',
		'movilTlf',
		'houseTlf',
		'mailUser',
		]
		labels = {
		'nameUser':'Primer Nombre',
		'lastName':'Apellidos',
		'dni': 'Documento De Identidad',
		'movilTlf':'Numero Movil de Contacto',
		'houseTlf': 'Numero Secundario',
		'mailUser':'Correo Electronico',
		'image':'Imagen de Perfil',

		
		}
		widgets = {
		'nameUser': TextInput(attrs={'class':'form-control', 
			  'disabled':True,
			  'autocomplete':'off',
			   'placeholder':'Ingrese El Primer Nombre Del Usuario'}),

		'lastName': TextInput(attrs={'class':'form-control', 
			  'disabled':True,
			  'autocomplete':'off',
			   'placeholder':'Ingrese El Apellido Del Usuario'}),

		'dni': TextInput(attrs={'class':'form-control', 
			  'disabled':True,
			  'autocomplete':'off',
			   'placeholder':'Ingrese El Documento De Identidad Del usuario'}),

		'movilTlf': TextInput(attrs={'class':'form-control', 
			  'disabled':True,
			  'autocomplete':'off',
			   'placeholder':'Ingrese El Numero de Contacto'}),

		'houseTlf': TextInput(attrs={'class':'form-control', 
			  'disabled':True,
			  'autocomplete':'off',
			   'placeholder':'Ingrese un numero de contacto alterno'}),

		'mailUser': EmailInput(attrs={'class':'form-control', 
			  'disabled':True,
			  'autocomplete':'off',
			   'placeholder':'Ingrese su correo electronico de contacto'}),
		'image': FileInput(attrs={'class':'', 
			  'disabled':True,
			  'autocomplete':'off',
			   'placeholder':'Ingrese su imagen de perfil'}),
		#'descriptionProduct': Textarea(attrs={'class':'form-control', 
		#	'required':True ,
		#	 'autofocus':True,
		#	  'autocomplete':'off',
		#	   ,'placeholder':'Direccion Principal Del Nuevo Proveedor',
		#	   'cols': 2, 
		#	   'rows': 6}),
		}
          
		exclude = ['user','birthdayDate', 'tipoUser', 'dateCreate', 'is_complete', 'image']  		
		
		
