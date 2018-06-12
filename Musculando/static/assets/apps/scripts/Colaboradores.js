
setInterval(function () {
	//console.log('miguel')
	if (parseInt($('#id_honorariosMensuales').val()) > 0) {
		//activa el check de honorarios
		//console.log('activo')
		$('#id_isHonorarios').prop('checked', true);
		$('#id_isHonorarios').val('True');
	}
	else
	{
		//console.log('desactivo')
		$('#id_isHonorarios').prop('checked', false);
		$('#id_isHonorarios').val('False');
	}
	if (parseInt($('#id_montoXClase').val()) >0) {
		$('#id_isMontoXClase').prop('checked', true);
		$('#id_isMontoXClase').val('True');
	}
	else {
		$('#id_isMontoXClase').prop('checked', false);
		$('#id_isMontoXClase').val('False');
	}
	if (parseInt($('#id_comisionXClase').val()) >0) {
		$('#id_isComison').prop('checked', true);
		$('#id_isComison').val('True');
	}
	else {
		$('#id_isComison').prop('checked', false);
		$('#id_isComison').val('False');
	}

	if (parseInt($('#id_presentimo').val()) >0) {
		$('#id_isPresentimo').prop('checked', true);
		$('#id_isPresentimo').val('True');
	}
	else {
		$('#id_isPresentimo').prop('checked', false);
		$('#id_isPresentimo').val('False');
	}



	if (parseInt($('#id_montoAguinaldo').val()) >0) {
		$('#id_isAguinaldo').prop('checked', true);
		$('#id_isAguinaldo').val('True');
	}
	else {
		$('#id_isAguinaldo').prop('checked', false);
		$('#id_isAguinaldo').val('False');
	}

	 }, 300);



















function EliminarColaborador2(id_colaborador,id_profile) {
	//obtener id
	//preguntar si lo eliminara 
	//eliminar
	//dar una respuesta 

	swal({
		  title: '¿Estas Seguro?',
		  text: "¿Estas Seguro de que deseas eliminar a este Colaborador?",
		  type: 'warning',
		  showCancelButton: true,
		  confirmButtonColor: '#3085d6',
		  cancelButtonColor: '#d33',
		  confirmButtonText: 'Si, Quiero Eliminarlo!'
		}).then(function (result) {
			if(result.value){
           	var screen = $('#loading-screen');
    		
           	//Ajax para eliminar el Plan
           	$.ajax({
		    // la URL para la petición
		    url : '/Colaboradores/Solicitud/Para/eliminar/Colaborador',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'id':id_colaborador,
		    	'id_profile':id_profile
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
					      'Hemos Borrado satisfactoriamente tu Colaborador.',
					      'success'
					    );
		        	location.href ="/Colaboradores/Lista/";
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al borrar su socio!", "error")
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



