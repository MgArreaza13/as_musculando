from django import forms
from django.forms import ModelForm, Media,TextInput, NumberInput,EmailInput,URLInput,PasswordInput,FileInput,Textarea,DateInput,DateTimeInput,Select
from django.forms import extras

from apps.Canchas.models import Cancha 
from apps.Canchas.models import ReservaCancha

class CanchaForm(forms.ModelForm):
    class Meta:
        model = Cancha
        fields = ['nameCancha','precioHora','description', 'image']
        exclude = ['dateCreate',]
        labels={
        	'nameCancha':'Nombre de la Cancha',
			'precioHora' :'Precio Por Hora',
			'description' :'Decripcion',
			'image' :'Imagen',
        }
        widgets = {
	        'nameCancha': TextInput(attrs={'class':'form-control', 
				  'required':'False',
				  'disabled':False,
				  'autocomplete':'off',
				   'placeholder':'Nombre de La cancha'}),

			'precioHora': NumberInput(attrs={'class':'form-control', 
				  'required':'False',
				  'disabled':False,
				  'autocomplete':'off',
				   'placeholder':'Descripcion del Ingreso'}),

			'description': Textarea(attrs={'class':'form-control', 
				'required':True ,
				 'autofocus':True,
				  'autocomplete':'off',
				   'placeholder':'Descripcion de la cancha',
				   'cols': 2, 
				   'rows': 6}),


			

			'tipoDeIngresos': Select(attrs={'class':'form-control', 
				  'required':'False',
				  'disabled':False,
				  'autocomplete':'off',
				   'placeholder':'Tipo de Ingreso'}),

			'image': FileInput(attrs={'class':'', 
				  'required':'False',
				  'disabled':False,
				  'autocomplete':'off',
				   'placeholder':'Imagen'}),

        }




class nuevaReservasForm(forms.ModelForm):
    class Meta:
        model = ReservaCancha
        fields = ['mail','nombre','telefono', 'statusTurn', 'cancha', 
        			'dateTurn', 'montoAPagar', 'description', 'observaciones']
        exclude = ['dateCreate', 'montoPagado', 'isPay', 'TipoReservas']
        labels={
        	'mail': 'Correo',
        	'nombre': 'Nombre',
        	'telefono': 'Numero Telefonico', 
        	'statusTurn': 'Estatus de la Reserva', 
        	'cancha': 'Cancha Reservada', 
        	'dateTurn': 'Fecha de Reserva', 
        	'montoAPagar': 'Monto a Pagar por la Reserva', 
        	'description': 'Descripcion', 
        	'observaciones': 'Observaciones'
        }
        widgets = {
	        'mail': EmailInput(attrs={'class':'form-control', 
				  'required':'False',
				  'disabled':False,
				  'autocomplete':'off',
				   'placeholder':'Correo Electronico'}),

	        'nombre': TextInput(attrs={'class':'form-control', 
				  'required':'False',
				  'disabled':False,
				  'autocomplete':'off',
				   'placeholder':'Ingrese su Nombre'}),

	        'telefono': TextInput(attrs={'class':'form-control', 
				  'required':'False',
				  'disabled':False,
				  'autocomplete':'off',
				   'placeholder':'Ingrese su numero Telefonico'}),

	        'statusTurn': Select(attrs={'class':'form-control', 
				  'required':'False',
				  'disabled':False,
				  'autocomplete':'off',
				   'placeholder':'Ingrese El Status con que desea guardar la reserva'}),

	        'cancha': Select(attrs={'class':'form-control', 
				  'required':'False',
				  'disabled':False,
				  'autocomplete':'off',
				   'placeholder':'Ingrese la cancha donde desea hacer la reserva'}),

	        'dateTurn': DateTimeInput(attrs={'class':'form-control', 
				  'required':'False',
				  'disabled':False,
				  'autocomplete':'off',
				   'placeholder':'Ingrese la fecha de su reserva '}),

			'montoAPagar': NumberInput(attrs={'class':'form-control', 
				  'required':'False',
				  'disabled':False,
				  'autocomplete':'off',
				   'placeholder':'Ingrese el monto a pagar de la reserva'}),

			'description': Textarea(attrs={'class':'form-control', 
				'required':True ,
				 'autofocus':True,
				  'autocomplete':'off',
				   'placeholder':'Descripcion de la Reserva',
				   'cols': 2, 
				   'rows': 6}),

			'observaciones': Textarea(attrs={'class':'form-control', 
				'required':True ,
				 'autofocus':True,
				  'autocomplete':'off',
				   'placeholder':'Observaciones sobre la Reserva',
				   'cols': 2, 
				   'rows': 6}),

        }





