function EnviarNuevoReporteDePago() {
	var usuario = $('#Usuario').val();
	var nombre = $('#Nombre').val();
	var apellido = $('#Apellido').val();
	var correo = $('#email').val();
	var tarifaMensual = $('#TarifaMensual').val();
	var MontoTafifaMensual = $('#MontoTarifaMensual').val();
	var Direccion = $('#Direccion').val();
	var screen = $('#loading-screen');
    configureLoadingScreen(screen);


	$.ajax({
		    // la URL para la petición
		    url : '/Caja/Nueva/Solicitud/Pago/De/Mensualidad/',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'usuario':usuario,
		    	'nombre':nombre,
		    	'apellido':apellido,
		    	'correo':correo,
		    	'tarifaMensual':tarifaMensual,
		    	'MontoTafifaMensual':MontoTafifaMensual,
		    	'Direccion':Direccion

		    },
		    // el tipo de información que se espera de respuesta
		    dataType : 'json',
		    // código a ejecutar si la petición es satisfactoria;
		    // la respuesta es pasada como argumento a la función
		    success : function(status) {
		    	if (status == 200) {
		    		//todo correcto 
		    		swal("Felicidades!", "Hemos Cargado Tu Pago Con Exito!", "success")
		        	location.href ="/";
		    	}
		    	else{
		    		swal("OOOh!", "Error!", "error")
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


function configureLoadingScreen(screen){
    $(document)
        .ajaxStart(function () {
            screen.fadeIn();
        })
        .ajaxStop(function () {
            screen.fadeOut();
        });
}
