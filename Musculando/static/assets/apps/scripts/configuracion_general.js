function EliminarFormaDePago(id) {
	swal({
		  title: '¿Estas Seguro?',
		  text: "¿Estas Seguro de que deseas eliminar esta forma de pago?",
		  type: 'warning',
		  showCancelButton: true,
		  confirmButtonColor: '#3085d6',
		  cancelButtonColor: '#d33',
		  confirmButtonText: 'Si, Quiero Eliminarla!'
		}).then(function (result) {
           if(result.value){
           	var screen = $('#loading-screen');
    		
           	//Ajax para eliminar el Plan
           	$.ajax({
		    // la URL para la petición
		    url : '/Configuracion/Forma/De/Pago/Solicitud/Eliminar/Registro/',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'id':id,
		    },
		    // el tipo de información que se espera de respuesta
		    dataType : 'json',
		    // código a ejecutar si la petición es satisfactoria;
		    // la respuesta es pasada como argumento a la función
		    success : function(status) {
		    	if (status == 200) {
		    		//todo correcto 
		    		swal(
					      'Borrado!',
					      'Hemos Borrado satisfactoriamente tu forma de pago.',
					      'success'
					    );
		        	location.href ="/Configuracion/";
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al borrar su forma de pago!", "error")
		    	}
		    },
		 
		    // código a ejecutar si la petición falla;
		    // son pasados como argumentos a la función
		    // el objeto de la petición en crudo y código de estatus de la petición
		    error : function(xhr, status) {
		        swal("OOOh!", "Hemos tenido un problema con el Servidor!", "error")
		    },
		 
		    // código a ejecutar sin importar si la petición falló o n
		});
           }
        });
}



function NuevaFormaDePago() {
 swal({
  html: '<h1>Forma de Pago</h1><h3 style="color:blue">Ingrese La forma de Pago que desea Aceptar</h3>',
  input: 'text',
  inputPlaceholder: 'Forma de pago',
  showCancelButton: true,
  inputValidator: (value) => {
  	if (value == '') {
  		return !value && 'Necesitas escribir algo!'
  	}
    else{
    	  	$.ajax({
		    // la URL para la petición
		    url : '/Configuracion/Forma/De/Pago/Solicitud/Nuevo/Registro/',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'nombreFormaPago':value,
		    },
		    // el tipo de información que se espera de respuesta
		    dataType : 'json',
		    // código a ejecutar si la petición es satisfactoria;
		    // la respuesta es pasada como argumento a la función
		    success : function(status) {
		    	if (status == 200) {
		    		//todo correcto 
		    		swal(
					      'Felicidades!',
					      'Agregamos Su Forma de Pago satisfactoriamente.',
					      'success'
					    );
		        	location.href ="/Configuracion/";
		    	}
		    	else if (status == 401) {
		    		//todo correcto 
		    		swal(
					      'Error!',
					      'Ya posees una forma de pago con ese nombre .',
					      'error'
					    );
		        	
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al cargar su forma de pago!", "error")
		    	}
		    },
		 
		    // código a ejecutar si la petición falla;
		    // son pasados como argumentos a la función
		    // el objeto de la petición en crudo y código de estatus de la petición
		    error : function(xhr, status) {
		        swal("OOOh!", "Hemos tenido un problema con el Servidor!", "error")
		    },
		 
		    // código a ejecutar sin importar si la petición falló o n
		});
    }
  }
})



}


function EditarFormaDePago(id) {
	$.ajax({
		    // la URL para la petición
		    url : '/Configuracion/Forma/De/Pago/Solicitud/Get/Registro/',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'id_forma_de_pago':id,
		    },
		    // el tipo de información que se espera de respuesta
		    dataType : 'json',
		    // código a ejecutar si la petición es satisfactoria;
		    // la respuesta es pasada como argumento a la función
		    success : function(formaDePago) {
		    	if (formaDePago) {
			    	swal({
					  html: '<h1>Editar Forma de Pago</h1><h3 style="color:blue">'+	formaDePago.formaDePago +'</h3>',
					  input: 'text',
					  inputPlaceholder: ''+formaDePago.formaDePago+'',
					  showCancelButton: true,
					  inputValidator: (value) => {
					  	if (value == '') {
					  		return !value && 'Necesitas escribir algo!'
					  	}
					    else{
			    	  	$.ajax({
					    // la URL para la petición
					    url : '/Configuracion/Forma/De/Pago/Solicitud/Update/Registro/',
					    // la información a enviar
					    // (también es posible utilizar una cadena de datos)
					    data : { 
					    	'id_forma_de_pago':id,
					    	'nombreFormaPago':value,
					    },
					    // el tipo de información que se espera de respuesta
					    dataType : 'json',
					    // código a ejecutar si la petición es satisfactoria;
					    // la respuesta es pasada como argumento a la función
					    success : function(status) {
					    	//console.log(status)
					    	if (status == 200) {
					    		//todo correcto 
					    		swal(
								      'Felicidades!',
								      'Agregamos Su Forma de Pago satisfactoriamente.',
								      'success'
								    );
					        	location.href ="/Configuracion/";
					    	}
					    	else if (status == 401) {
					    		//todo correcto 
					    		swal(
								      'Error!',
								      'Ya posees una forma de pago con ese nombre .',
								      'error'
								    );
					        	
					    	}
					    	else{
					    		swal("OOOh!", "Hemos tenido un problema al cargar su forma de pago!", "error")
					    	}
					    },
					 
					    // código a ejecutar si la petición falla;
					    // son pasados como argumentos a la función
					    // el objeto de la petición en crudo y código de estatus de la petición
					    error : function(xhr, status) {
					        swal("OOOh!", "Hemos tenido un problema con el Servidor!", "error")
					    },
					 
					    // código a ejecutar sin importar si la petición falló o n
					});
			    }
			  }
			})
		   }
		    	
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al cargar su forma de pago!", "error")
		    	}
		    },
		 
		    // código a ejecutar si la petición falla;
		    // son pasados como argumentos a la función
		    // el objeto de la petición en crudo y código de estatus de la petición
		    error : function(xhr, status) {
		        swal("OOOh!", "Hemos tenido un problema con el Servidor!", "error")
		    },
		 
		    // código a ejecutar sin importar si la petición falló o n
		});
}