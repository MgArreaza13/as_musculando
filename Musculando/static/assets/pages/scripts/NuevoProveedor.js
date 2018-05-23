function NuevoProveedor() {
	var NombreValido = false;
	var CorreoValido = false;
	var regex = /[\w-\.]{2,}@([\w-]{2,}\.)*([\w-]{2,}\.)[\w-]{2,4}/;
	var Nombre = $('#Nombre').val();
	var Correo = $('#Correo').val();
	var RazonSocial = $('#RazonSocial').val();
	var Telefono = $('#Telefono').val();
	var Direccion = $('#Direccion').val();
	//input del Nombre Vacio 
	if (Nombre == '') {
		//Nombre Invalido
		$('#textoProveedor').removeClass('hidden');
		NombreValido = false;
	}
	else{
		//Nombre Valido
		$('#textoProveedor').addClass('hidden');
		NombreValido = true;
	}
	//Correo Vacio
    if (regex.test($('#Correo').val().trim())) {
    	//correo valido
        $('#CorreoProveedor').addClass('hidden');
        CorreoValido = true;
    } else {
        $('#CorreoProveedor').removeClass('hidden');
        CorreoValido = false;
    }
    //enviar el formulario
    if (NombreValido == true && CorreoValido == true) {
    	 var screen = $('#loading-screen');
    	configureLoadingScreen(screen);
    	$.ajax({
		    // la URL para la petición
		    url : '/Proveedores/Nueva/Peticion/de/Nuevo/Proveedor',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'Nombre':Nombre,
		    	'Correo':Correo,
		    	'RazonSocial':RazonSocial,
		    	'Telefono':Telefono,
		    	'Direccion':Direccion,
		    },
		    // el tipo de información que se espera de respuesta
		    dataType : 'json',
		    // código a ejecutar si la petición es satisfactoria;
		    // la respuesta es pasada como argumento a la función
		    success : function(status) {
		    	if (status == 200) {
		    		//todo correcto 
		    		swal("Felicidades!", "Hemos Cargado Tu Registro Con Exito!", "success")
		        	location.href ="/Proveedores/Lista/";
		    	}
		    	else{
		    		swal("OOOh!", "Proveedor Ya existe en la Base de Datos!", "error")
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
    //no envio el formulario
    else{
    	swal("OOOh!", "Corrije Los siguientes Errores!", "error")
    }
}




function UpdateProveedor(id) {
	var NombreValido = false;
	var CorreoValido = false;
	var regex = /[\w-\.]{2,}@([\w-]{2,}\.)*([\w-]{2,}\.)[\w-]{2,4}/;
	var Nombre = $('#Nombre').val();
	var Correo = $('#Correo').val();
	var RazonSocial = $('#RazonSocial').val();
	var Telefono = $('#Telefono').val();
	var Direccion = $('#Direccion').val();
	//input del Nombre Vacio 
	if (Nombre == '') {
		//Nombre Invalido
		$('#textoProveedor').removeClass('hidden');
		NombreValido = false;
	}
	else{
		//Nombre Valido
		$('#textoProveedor').addClass('hidden');
		NombreValido = true;
	}
	//Correo Vacio
    if (regex.test($('#Correo').val().trim())) {
    	//correo valido
        $('#CorreoProveedor').addClass('hidden');
        CorreoValido = true;
    } else {
        $('#CorreoProveedor').removeClass('hidden');
        CorreoValido = false;
    }
    //enviar el formulario
    if (NombreValido == true && CorreoValido == true) {
    	 var screen = $('#loading-screen');
    	configureLoadingScreen(screen);
    	$.ajax({
		    // la URL para la petición
		    url : '/Proveedores/Nueva/Peticion/de/Update/Proveedor',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'id':id,
		    	'Nombre':Nombre,
		    	'Correo':Correo,
		    	'RazonSocial':RazonSocial,
		    	'Telefono':Telefono,
		    	'Direccion':Direccion,
		    },
		    // el tipo de información que se espera de respuesta
		    dataType : 'json',
		    // código a ejecutar si la petición es satisfactoria;
		    // la respuesta es pasada como argumento a la función
		    success : function(status) {
		    	if (status == 200) {
		    		//todo correcto 
		    		swal("Felicidades!", "Hemos Cargado Tu Registro Con Exito!", "success")
		        	location.href ="/Proveedores/Lista/";
		    	}
		    	else{
		    		swal("OOOh!", "Proveedor Ya existe en la Base de Datos!", "error")
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
    //no envio el formulario
    else{
    	swal("OOOh!", "Corrije Los siguientes Errores!", "error")
    }
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