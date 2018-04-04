var Nombre_Validate = false;
var Precio_Validate = false;
var Promocion_Anual = false;

function Modal() {
	$('#Nombre').val('');
	$('#precio').val('');
	$('#precioAnualinput').val('');
	$('#Descripcion').val('');
	$("#ActualizarPlan").addClass('hidden');
	$("#GuardarPlan").removeClass('hidden');
	$('#NuevoPlanNombre').addClass('hidden');
	$('#PrecioNuevoPlan').addClass('hidden');
	$("#responsive").modal("show");
}

function EnviarDatosDePlan() {
	var Nombre = $('#Nombre').val();
	var Precio = $('#precio').val();
	var PrecioAnual = $('#precioAnualinput').val();
	var Descripcion = $('#Descripcion').val();
	if (Nombre == '') {
		//Nombre Invalido
		$('#NuevoPlanNombre').removeClass('hidden');
		Nombre_Validate  = false;
	}else{
		//Nombre Valido
		$('#NuevoPlanNombre').addClass('hidden');
		Nombre_Validate = true;}
	if (PrecioAnual == '') {
		//Nombre Invalido
		$('#PrecioAnualPlan').removeClass('hidden');
		Promocion_Anual  = false;
	}else{
		//Nombre Valido
		$('#PrecioAnualPlan').addClass('hidden');
		Promocion_Anual = true;}
	if (Precio == '') {
		//Nombre Invalido
		$('#PrecioNuevoPlan').removeClass('hidden');
		Precio_Validate = false;
	}else{
		//Nombre Valido
		$('#PrecioNuevoPlan').addClass('hidden');
		Precio_Validate = true;}
	if (Nombre_Validate == true && Precio_Validate == true && Promocion_Anual == true) {
	    $("#responsive").modal("hide");
    	 var screen = $('#loading-screen');
    	configureLoadingScreen(screen);

    	$.ajax({
		    // la URL para la petición
		    url : '/Configuracion/Planes/Solicitud/Nuevo/Registro/',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'Nombre':Nombre,
		    	'Precio':Precio,
		    	'Descripcion':Descripcion,
		    	'PrecioAnual':PrecioAnual,
		    },
		    // el tipo de información que se espera de respuesta
		    dataType : 'json',
		    // código a ejecutar si la petición es satisfactoria;
		    // la respuesta es pasada como argumento a la función
		    success : function(status) {
		    	if (status == 200) {
		    		//todo correcto 
		    		swal("Felicidades!", "Hemos Cargado Tu Registro Con Exito!", "success")
		        	location.href ="/Configuracion/Planes/Lista/";
		    	}
		    	else{
		    		swal("OOOh!", "Ya posees un Plan con este mismo nombre!", "error")
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
    	//swal("OOOh!", "Corrije Los siguientes Errores!", "error")
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

function EliminarPlan(id) {
	swal({
		  title: '¿Estas Seguro?',
		  text: "¿Estas Seguro de que deseas eliminar este plan?",
		  type: 'warning',
		  showCancelButton: true,
		  confirmButtonColor: '#3085d6',
		  cancelButtonColor: '#d33',
		  confirmButtonText: 'Si, Quiero Eliminarlo!'
		}).then(function (result) {
           if(result.value){
           	var screen = $('#loading-screen');
    		configureLoadingScreen(screen);
           	//Ajax para eliminar el Plan
           	$.ajax({
		    // la URL para la petición
		    url : '/Configuracion/Planes/Solicitud/Eliminar/Registro/',
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
					      'Hemos Borrado satisfactoriamente tu archivo.',
					      'success'
					    );
		        	location.href ="/Configuracion/Planes/Lista/";
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
        });
}


function EditarPlan(id) {
	//get datos server.
	var screen = $('#loading-screen');
   	configureLoadingScreen(screen);
	$.ajax({
		    // la URL para la petición
		    url : '/Configuracion/Planes/Solicitud/Get/Registro/',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'id':id,
		    },
		    // el tipo de información que se espera de respuesta
		    dataType : 'json',
		    // código a ejecutar si la petición es satisfactoria;
		    // la respuesta es pasada como argumento a la función
		    success : function(plan) {
		    	if (plan) {
		    		//todo correcto 
		    		$('#Nombre').val(plan.nombrePlan);
		    		$('#precio').val(plan.precioPlan);
		    		$('#precioAnualinput').val(plan.montoAnal);
		    		$('#Descripcion').val(plan.descripcionPlan);
		    		$("#ActualizarPlan").removeClass('hidden');
		    		$("#GuardarPlan").addClass('hidden');
		    		$('#NuevoPlanNombre').addClass('hidden');
					$('#PrecioNuevoPlan').addClass('hidden');
		    		$("#ActualizarPlan").val(id);
		    		$("#responsive").modal("show");
	
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

function UpdatePlan(id) {
	var Nombre = $('#Nombre').val();
	var Precio = $('#precio').val();
	var MontoAnual = $('#precioAnualinput').val();
	var Descripcion = $('#Descripcion').val();
	if (Nombre == '') {
		//Nombre Invalido
		$('#NuevoPlanNombre').removeClass('hidden');
		Nombre_Validate  = false;
	}else{
		//Nombre Valido
		$('#NuevoPlanNombre').addClass('hidden');
		Nombre_Validate = true;}
	if (Precio == '') {
		//Nombre Invalido
		$('#PrecioNuevoPlan').removeClass('hidden');
		Precio_Validate = false;
	}else{
		//Nombre Valido
		$('#PrecioNuevoPlan').addClass('hidden');
		Precio_Validate = true;}
	if (MontoAnual == '') {
		//Nombre Invalido
		$('#PrecioAnualPlan').removeClass('hidden');
		Promocion_Anual  = false;
	}else{
		//Nombre Valido
		$('#PrecioAnualPlan').addClass('hidden');
		Promocion_Anual = true;}

	if (Nombre_Validate == true && Precio_Validate == true && Promocion_Anual == true) {
	    $("#responsive").modal("hide");
    	 var screen = $('#loading-screen');
    	configureLoadingScreen(screen);

    	$.ajax({
		    // la URL para la petición
		    url : '/Configuracion/Planes/Solicitud/Update/Registro/',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'id':id,
		    	'Nombre':Nombre,
		    	'MontoAnual':MontoAnual,
		    	'Precio':Precio,
		    	'Descripcion':Descripcion,
		    },
		    // el tipo de información que se espera de respuesta
		    dataType : 'json',
		    // código a ejecutar si la petición es satisfactoria;
		    // la respuesta es pasada como argumento a la función
		    success : function(status) {
		    	//console.log(status)
		    	if (status == 200) {
		    		//todo correcto 
		    		swal("Felicidades!", "Hemos Cargado Tu Registro Con Exito!", "success")
		        	location.href ="/Configuracion/Planes/Lista/";
		    	}
		    	else{
		    		swal("OOOh!", "Ya posees un Plan con este mismo nombre!", "error")
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
    	//swal("OOOh!", "Corrije Los siguientes Errores!", "error")
    }
}





