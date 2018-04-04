
function Get_formas_de_pago() {
	var response_json;
	 $.ajax({
		    // la URL para la petición
		    url : '/Configuracion/Forma/De/Pago/Solicitud/Get/',
		    dataType : 'json',
		    // código a ejecutar si la petición es satisfactoria;
		    // la respuesta es pasada como argumento a la función
		    success : function(data) {
		    	response_json = data
		    	
		    }
		 
		    // código a ejecutar si la petición falla;
		    // son pasados como argumentos a la función
		    // el objeto de la petición en crudo y código de estatus de la petición
		   
		 
		    // código a ejecutar sin importar si la petición falló o n
		});	

	 return response_json;
}

function Eliminar(id) {
	swal({
		  title: '¿Estas Seguro?',
		  text: "¿Estas Seguro de que deseas eliminar este Socio?",
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
		    url : '/Socios/Nueva/Peticion/de/Eliminacion/de/Socios',
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
					      'Hemos Borrado satisfactoriamente tu Socio.',
					      'success'
					    );
		        	location.href ="/Socios/Lista/";
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


function Desactivar(id_socio) {
	swal({
		  title: '¿Estas Seguro?',
		  text: "¿Estas Seguro de que deseas Desactivar este Socio?",
		  type: 'warning',
		  showCancelButton: true,
		  confirmButtonColor: '#3085d6',
		  cancelButtonColor: '#d33',
		  confirmButtonText: 'Si, Quiero Desactivarlo!'
		}).then(function (result) {
           if(result.value){
           	var screen = $('#loading-screen');
    		
           	//Ajax para eliminar el Plan
           	$.ajax({
		    // la URL para la petición
		    url : '/Socios/Nueva/Peticion/de/Desactivar',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'id':id_socio,
		    },
		    // el tipo de información que se espera de respuesta
		    dataType : 'json',
		    // código a ejecutar si la petición es satisfactoria;
		    // la respuesta es pasada como argumento a la función
		    success : function(status) {
		    	if (status == 200) {
		    		//todo correcto 
		    		swal(
					      'Desactivado!',
					      'Hemos Desactivado satisfactoriamente tu Socio.',
					      'success'
					    );
		        	location.href ="/Socios/Lista/";
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

function Activar(id_socio) {
	swal({
		  title: '¿Estas Seguro?',
		  text: "¿Estas Seguro de que deseas Activar este Socio?",
		  type: 'warning',
		  showCancelButton: true,
		  confirmButtonColor: '#3085d6',
		  cancelButtonColor: '#d33',
		  confirmButtonText: 'Si, Quiero Activarlo!'
		}).then(function (result) {
           if(result.value){
           	var screen = $('#loading-screen');
    		
           	//Ajax para eliminar el Plan
           	$.ajax({
		    // la URL para la petición
		    url : '/Socios/Nueva/Peticion/de/Activar',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'id':id_socio,
		    },
		    // el tipo de información que se espera de respuesta
		    dataType : 'json',
		    // código a ejecutar si la petición es satisfactoria;
		    // la respuesta es pasada como argumento a la función
		    success : function(status) {
		    	if (status == 200) {
		    		//todo correcto 
		    		swal(
					      'Activado!',
					      'Hemos Activado satisfactoriamente tu Socio.',
					      'success'
					    );
		        	location.href ="/Socios/Lista/";
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al Activar al socio!", "error")
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

function Reportar_Pago(id) {
	var screen = $('#loading-screen');
    configureLoadingScreen(screen);

    $.ajax({
		    // la URL para la petición
		    url : '/Socios/Nueva/Peticion/de/Obtener/Datos/Socios',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'id_socio':id,
		    },
		    // el tipo de información que se espera de respuesta
		    dataType : 'json',
		    // código a ejecutar si la petición es satisfactoria;
		    // la respuesta es pasada como argumento a la función
		    success : function(data) {
		    	if (data) {
		    		//todo correcto 
		    		console.log(data)
		    		 $('#Usuario').val(data.username);
					 $('#Nombre').val(data.name);
					 $('#Apellido').val(data.lastname);
					 $('#email').val(data.mail);
					 $('#TarifaMensual').val(data.plan);
					 $('#MontoTarifaMensual').val(data.monto_plan);
			    		$('#Listado').addClass('hidden');
						$('#Pago_Template').removeClass('hidden');
						$('#Pago_Template').addClass('animated bounceInUp');
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

function CerrarPagoTemplate() {
	$('#Pago_Template').addClass('hidden');
	$('#Listado').removeClass('hidden');
	$('#Listado').addClass('animated bounceInRight');
	$('#Usuario').val('');
	$('#Nombre').val('');
	$('#Apellido').val('');
	$('#email').val('');
	$('#TarifaMensual').val('');
	$('#MontoTarifaMensual').val('');
}


function EnviarNuevoReporteDePago2() {
	var usuario = $('#Usuario').val();
	var nombre = $('#Nombre').val();
	var apellido = $('#Apellido').val();
	var correo = $('#email').val();
	var tarifaMensual = $('#TarifaMensual').val();
	var MontoTafifaMensual = $('#MontoTarifaMensual').val();
	var Direccion = $('#Direccion').val();


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
		        	location.href ="/Socios/Lista/";
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



function ReportePago(id) {
	var myArrayOfThings;
	$.ajax({
		    // la URL para la petición
		    url : '/Configuracion/Forma/De/Pago/Solicitud/Get/',
		    dataType : 'json',
		    // código a ejecutar si la petición es satisfactoria;
		    // la respuesta es pasada como argumento a la función
		    success : function(data) {
		    	
		    	myArrayOfThings  = data
		    	var options = {};
			    $.map(myArrayOfThings,function(o,query) {options[o.forma_de_pago] = o.forma_de_pago;});
			      swal.setDefaults({
			          input: 'text',
			          confirmButtonText: 'Siguiente &rarr;',
			          showCancelButton: true,
			          progressSteps: ['1', '2']
			        })
			      //console.log(options);
			        var steps = [
			          {
			           	 title: 'Seleccione la forma que desea activar',
						  input: 'select',
						  inputOptions: {
						    'Anual': 'Anual',
						    'Mensual': 'Mensual',
						  },
						  inputPlaceholder: 'Activar Anual o Mensual',
			          },
			        {
			            title: 'Seleccione un metodo de pago',
			            input: 'select',
			            inputOptions: options,
			            inputPlaceholder: 'metodos de pago',
			          },


			          
			        ]

			        swal.queue(steps).then(function (result) {
			        	if (result.value[0] != '' && result.value[1] != '' ){
			        		mensual_anual = result.value[0];
			        		forma_pago = result.value[1];
			        		swal.resetDefaults()
			        	if (result.value[0] == "Anual") {
						    swal({
						  title: '¿Estas Seguro?',
						  text: "¿Estas Seguro de que deseas Activar este Socio por todo el año?",
						  type: 'warning',
						  showCancelButton: true,
						  confirmButtonColor: '#3085d6',
						  cancelButtonColor: '#d33',
						  confirmButtonText: 'Si, Quiero Activarlo Anual!'
						}).then(function (result) {
							//console.log(result)
				           if(result.value){
				           	//console.log('dije que si ');
				    		$.ajax({
			                    url: '/Socios/Nueva/Peticion/de/Activar/Socio/',
			                    data: {
			                      'id_socio':id,
			                      'mensual_anual': mensual_anual,
			                      'forma_pago':forma_pago,
			                  },
			                  dataType: 'json',
			                  success: function (status) {
			                     swal({
			                        title: 'Hemos Cargado de manera exitosa su pago !',
			                        confirmButtonText: 'Aceptar!'
			                      })
			                     location.reload(); 
			                }
			            });
				           	
				           }
				        });
						  }
						else if (result.value[0] == "Mensual") {
						    swal({
						  title: '¿Estas Seguro?',
						  text: "¿Estas Seguro de que deseas Activar este Socio por todo el mes?",
						  type: 'warning',
						  showCancelButton: true,
						  confirmButtonColor: '#3085d6',
						  cancelButtonColor: '#d33',
						  confirmButtonText: 'Si, Quiero Activarlo Mensual!'
						}).then(function (result) {
							console.log(result)
				           if(result.value){
				           	//console.log('dije que si ');
				    		$.ajax({
			                    url: '/Socios/Nueva/Peticion/de/Activar/Socio/',
			                    data: {
			                      'id_socio':id,
			                      'mensual_anual': mensual_anual,
			                      'forma_pago':forma_pago,
			                  },
			                  dataType: 'json',
			                  success: function (status) {
			                     swal({
			                        title: 'Hemos Cargado de manera exitosa su pago !',
			                        confirmButtonText: 'Aceptar!'
			                      })
			                     location.reload(); 
			                }
			            });
				           	
				           }
				        });
						  }

			        	}
			        	else{
			        		swal.resetDefaults()
			        		swal("OOOh!", "Hemos tenido un problema al verificar sus datos!", "error")



			        	}
			        	
			               
			                

			        }, function () {
			          swal.resetDefaults()
			        })
		    	
		    	
		    }
		 
		    // código a ejecutar si la petición falla;
		    // son pasados como argumentos a la función
		    // el objeto de la petición en crudo y código de estatus de la petición
		   
		 
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


