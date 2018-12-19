function NuevoTipoDeEgreso() {
 swal({
  html: '<h2>Añadir Tipo de Egreso</h2><h4 style="color:blue">Ingrese el tipo de Egreso que desea registrar</h4>',
  input: 'text',
  inputPlaceholder: 'Tipo De Egreso',
  showCancelButton: true,
  inputValidator: (value) => {
  	if (value == '') {
  		return !value && 'Necesitas escribir algo!'
  	}
    else{
    	  	$.ajax({
		    // la URL para la petición
		    url : '/configuracion/Tipo/De/Egreso/Solicitud/Nuevo/Registro/',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'TipoDeEgreso':value,
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
					      'Agregamos Su Tipo de Egreso satisfactoriamente.',
					      'success'
					    );
		        	location.href ="/configuracion/";
		    	}
		    	else if (status == 401) {
		    		
		    		swal(
					      'Error!',
					      'Ya posees un tipo de Egreso con ese nombre .',
					      'error'
					    );
		        	
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al cargar su tipo de Egreso!", "error")
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