function Verdescripcion(id) {
	//get datos server.
	var screen = $('#loading-screen');
   	configureLoadingScreen(screen);
	$.ajax({
		    // la URL para la petición
		    url : '/Configuracion/Terminos/Solicitud/Get/Registro/',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'id':id,
		    },
		    // el tipo de información que se espera de respuesta
		    dataType : 'json',
		    // código a ejecutar si la petición es satisfactoria;
		    // la respuesta es pasada como argumento a la función
		    success : function(termino) {
		    	if (termino) {
		    		//todo correcto 
		    		$('#Nombre').val(termino.nameTerminos);
		    		
		    		
		    		$('#Desc').text(termino.descripcion);
		    		$("#myModal").modal("show");
		    		
	
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al borrar su plan!", "error")
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