$('#id_montoAguinaldo').removeAttr('disabled', 'disabled');
setInterval(function () {
	//console.log('miguel')
	if (parseInt($('#id_honorariosMensuales').val()) > 0) {
		//activa el check de honorarios
		//console.log('activo')
		$('#id_isHonorarios').prop('checked', true);
		$('#id_isHonorarios').val('True');
		var aguinaldo = parseInt($('#id_honorariosMensuales').val()) / 2;
		$('#id_montoAguinaldo').val(aguinaldo);
	}
	
	
	else
	{
		//console.log('desactivo')
		$('#id_isHonorarios').prop('checked', false);
		$('#id_isHonorarios').val('False');
		$('#id_montoAguinaldo').val(0);

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






function PagarCuentaColaboradores() {
	//obtener id
	//preguntar si lo eliminara 
	//eliminar
	//dar una respuesta 

	swal({
		  title: '¿Estas Seguro?',
		  text: "¿Estas Seguro que deseas pagar el monto total de la cuenta de colaboradores? " +
		  		"este proceso se hara en segundo plano, ya que puede tardar un poco el proceso. " +
		  		"Pero se le avisara tan pronto haya terminado" ,
		  type: 'warning',
		  showCancelButton: true,
		  confirmButtonColor: '#3085d6',
		  cancelButtonColor: '#d33',
		  confirmButtonText: 'Si, Quiero Pagarlo!'
		}).then(function (result) {
			if(result.value){

				$.ajax({
		    // la URL para la petición
		    url : '/Colaboradores/Solicitud/Para/Procesar/Liquidacion/de/Colaboradores',
		    
		    dataType : 'json',
		    
		    success : function(status) {
		    	if (status == 200) {
		    		//todo correcto 
		    		swal(
					      'Proceso!',
					      'Estamos procesando los pagos, le informaremos a penas terminemos.',
					      'success'
					    );
		        	location.href ="/";
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema con su peticion", "error")
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




function LiquidarColaborador(colaborador_id) {
	swal({
		  title: '¿Estas Seguro?',
		  text: "¿Estas Seguro de que deseas Liquidar a este Colaborador?",
		  type: 'warning',
		  showCancelButton: true,
		  confirmButtonColor: '#3085d6',
		  cancelButtonColor: '#d33',
		  confirmButtonText: 'Si, Quiero Liquidarlo!'
		}).then(function (result) {
			if(result.value){
    		
           	//Ajax para eliminar el Plan
           	$.ajax({
		    // la URL para la petición
		    url : '/Colaboradores/Solicitud/Get/Colaborador',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'id':colaborador_id,
		    },
		    // el tipo de información que se espera de respuesta
		    dataType : 'json',
		    // código a ejecutar si la petición es satisfactoria;
		    // la respuesta es pasada como argumento a la función
		    success : function(dataUser) {
		    	if (dataUser) {
		    		if(dataUser[0].fields.isPresentimo == true){
		    			//tiene el presentimo activado
		    			presentimo_ = parseFloat(dataUser[0].fields.presentimo);
		    			deuda_ = parseFloat(dataUser[0].fields.cuentaColaborador);
		    			deudatotal = presentimo_ + deuda_;
		    			swal.setDefaults({
					          input: 'text',
					          confirmButtonText: 'Siguiente &rarr;',
					          showCancelButton: true,
					          progressSteps: ['1','2']
					        })
					      //console.log(options);
					        var steps = [
					        
					          {
					           	 html: '<h2 style="font-size:34px;">EL Colaborador posee una <br/> deduda de <br />' +
					           	 		' <spam style="color:blue; font-size:50px;"> $'+dataUser[0].fields.cuentaColaborador +'</spam>'+
					           	 		'<h2 style="font-size:24px;">Ingrese el monto que desea abonar a su cuenta corriente</h2>'+
					           	 		'<spam style="font-size:20px;color:red;">Recordando que los decimales son con <br /> el .(PUNTO) ejemplo "212.10"</spam>',
								  
								  inputPlaceholder: 'Ingrese el Monto a Abonar al Colaborador',
					          },
					          {
					           	 html: '<h2>Ademas del Monto de la Deuda del Colaborador, el mismo posee un presentimo pendiente por pagar '+
					           	 		'por un monto de <br /> <spam style="color:blue; font-size:50px;">$' + dataUser[0].fields.presentimo+'</spam>'+
					           	 		'<br />desea Pagar el mismo y sumarlo al abono del colaborador </h2>',
								  input: 'select',
								  inputOptions: {
								    'Si': 'Si',
								    'No': 'No',
								  },
								  inputPlaceholder: 'Pagar Presentimo',
					          },
					        ]

					        swal.queue(steps).then(function (result) {
					        	
					        	abono_colaborador = parseFloat(result.value[0]);
					        	

					        	if (result.value[0] != '' && result.value[1] != '' && isNaN(abono_colaborador) == false){
					        		
					        		if (result.value[1] == 'Si') {
					        			//pagar Presentimo

					        		cuenta = parseFloat(dataUser[0].fields.cuentaColaborador);
					        		deuda = cuenta - abono_colaborador;
					        		cuentaTotalColaborador = abono_colaborador + presentimo_;
					        		swal.resetDefaults()

					        		swal({
									  title: 'Abono De Colaborador',
									  html: '<h3>¿Estas seguro que desea abonar el monto de <spam style="color:blue; font-size:30px;">$'+
									  		abono_colaborador+ '</spam> mas el presentimo de <spam style="color:blue; font-size:30px;">$'+dataUser[0].fields.presentimo+ '</spam> en total le'+
									  		' pagaremos al colaborador <spam style="color:blue; font-size:30px;">$'+cuentaTotalColaborador+
									  		 '</spam>  y quedar restandole al colaborador '+
									  		'el monto de <spam style="color:red; font-size:30px;">$'+deuda+ ' de honorario</spam></h3>',
									  type: 'warning',
									  showCancelButton: true,
									  confirmButtonColor: '#3085d6',
									  cancelButtonColor: '#d33',
									  confirmButtonText: 'Si, Quiero Pagarlo!'
									}).then(function (result) {
							           if(result.value){
							           	var screen = $('#loading-screen');
							    		
							           	//Ajax para eliminar el Plan
							           	$.ajax({
									    // la URL para la petición
									    url : '/Colaboradores/Solicitud/Para/Procesar/Liquidacion/de/Colaboradores',
									    // la información a enviar
									    // (también es posible utilizar una cadena de datos)
									    data : { 
									    	'id':colaborador_id,
									    	'abono':abono_colaborador,
									    	'pagar_presentimo':'Si'
									    },
									    // el tipo de información que se espera de respuesta
									    dataType : 'json',
									    // código a ejecutar si la petición es satisfactoria;
									    // la respuesta es pasada como argumento a la función
									    success : function(status) {
									    	if (status == 200) {
									    		//todo correcto 
									    		swal(
												      'Abono Exitoso!',
												      'Hemos Abonado Exitosamente el monto al colaborador.',
												      'success'
												    );
									        	location.href ="/Colaboradores/Lista/";
									    	}
									    	else{
									    		swal("OOOh!", "Hemos tenido un problema al desactivar al socio!", "error")
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
					        		else if (result.value[1] == 'No') {
					        			// No quiere Pagar presentimo
					        		cuenta = parseFloat(dataUser[0].fields.cuentaColaborador);
					        		deuda = cuenta - abono_colaborador
					        		swal.resetDefaults()

					        		swal({
									  title: 'Abono De Colaborador',
									  html: '<h3>¿Estas seguro que desea abonar el monto de <spam style="color:blue; font-size:30px;">$'+
									  		abono_colaborador+ '</spam> y quedar restandole al colaborador '+
									  		'el monto de <spam style="color:red; font-size:30px;">$'+deuda+ '</spam></h3>',
									  type: 'warning',
									  showCancelButton: true,
									  confirmButtonColor: '#3085d6',
									  cancelButtonColor: '#d33',
									  confirmButtonText: 'Si, Quiero Pagarlo!'
									}).then(function (result) {
							           if(result.value){
							           	var screen = $('#loading-screen');
							    		
							           	//Ajax para eliminar el Plan
							           	$.ajax({
									    // la URL para la petición
									    url : '/Colaboradores/Solicitud/Para/Procesar/Liquidacion/de/Colaboradores',
									    // la información a enviar
									    // (también es posible utilizar una cadena de datos)
									    data : { 
									    	'id':colaborador_id,
									    	'abono':abono_colaborador,
									    	'pagar_presentimo':'No'
									    },
									    // el tipo de información que se espera de respuesta
									    dataType : 'json',
									    // código a ejecutar si la petición es satisfactoria;
									    // la respuesta es pasada como argumento a la función
									    success : function(status) {
									    	if (status == 200) {
									    		//todo correcto 
									    		swal(
												      'Abono Exitoso!',
												      'Hemos Abonado Exitosamente el monto al colaborador.',
												      'success'
												    );
									        	location.href ="/Colaboradores/Lista/";
									    	}
									    	else{
									    		swal("OOOh!", "Hemos tenido un problema al desactivar al socio!", "error")
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
					        	
								

					        	}
					        	else{
					        		
					        		swal.resetDefaults()
					        		//swal("OOOh!", "Hemos tenido un problema al verificar sus datos!", "error")



					        	}
					        	
					               
					                

					        }, function () {
					          swal.resetDefaults()
					        })










		    		}
		    		else if(dataUser[0].fields.isPresentimo == false){
		    			//tiene el presentimo desactivado
		    			
					      swal.setDefaults({
					          input: 'text',
					          confirmButtonText: 'Siguiente &rarr;',
					          showCancelButton: true,
					          progressSteps: ['1',]
					        })
					      //console.log(options);
					        var steps = [
					          {
					           	 html: '<h2 style="font-size:34px;">EL Colaborador posee una <br/> deduda de </h2>' +
					           	 		' <h1 style="color:blue"> $'+dataUser[0].fields.cuentaColaborador +'</h1>'+
					           	 		'<h2 style="font-size:24px;">Ingrese el monto que desea abonar a su cuenta corriente</h2>'+
					           	 		'<h3 style="font-size:20px;color:red;">Recordando que los decimales son con <br /> el .(PUNTO) ejemplo "212.10"</h3>',
								  
								  inputPlaceholder: 'Ingrese el Monto a Abonar al Colaborador',
					          },
					        ]

					        swal.queue(steps).then(function (result) {
					        	
					        	abono_colaborador = parseFloat(result.value[0]);
					        	

					        	if (result.value[0] != '' && isNaN(abono_colaborador) == false){
					        		cuenta = parseFloat(dataUser[0].fields.cuentaColaborador);
					        		deuda = cuenta - abono_colaborador
					        		swal.resetDefaults()

					        		swal({
									  title: 'Abono De Colaborador',
									  html: '<h3>¿Estas seguro que desea abonar el monto de <spam style="color:blue; font-size:30px;">$'+
									  		abono_colaborador+ '</spam> y quedar restandole al colaborador '+
									  		'el monto de <spam style="color:red; font-size:30px;">$'+deuda+ '</spam></h3>',
									  type: 'warning',
									  showCancelButton: true,
									  confirmButtonColor: '#3085d6',
									  cancelButtonColor: '#d33',
									  confirmButtonText: 'Si, Quiero Pagarlo!'
									}).then(function (result) {
							           if(result.value){
							           	var screen = $('#loading-screen');
							    		
							           	//Ajax para eliminar el Plan
							           	$.ajax({
									    // la URL para la petición
									    url : '/Colaboradores/Solicitud/Para/Procesar/Liquidacion/de/Colaboradores',
									    // la información a enviar
									    // (también es posible utilizar una cadena de datos)
									    data : { 
									    	'id':colaborador_id,
									    	'abono':abono_colaborador,
									    	'pagar_presentimo':'No'
									    },
									    // el tipo de información que se espera de respuesta
									    dataType : 'json',
									    // código a ejecutar si la petición es satisfactoria;
									    // la respuesta es pasada como argumento a la función
									    success : function(status) {
									    	if (status == 200) {
									    		//todo correcto 
									    		swal(
												      'Abono Exitoso!',
												      'Hemos Abonado Exitosamente el monto al colaborador.',
												      'success'
												    );
									        	location.href ="/Colaboradores/Lista/";
									    	}
									    	else{
									    		swal("OOOh!", "Hemos tenido un problema al desactivar al socio!", "error")
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
					        	else{
					        		
					        		swal.resetDefaults()
					        		//swal("OOOh!", "Hemos tenido un problema al verificar sus datos!", "error")



					        	}
					        	
					               
					                

					        }, function () {
					          swal.resetDefaults()
					        })
		    	
		    	


		    			
		    












		    		}
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al borrar su socio!", "error");
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