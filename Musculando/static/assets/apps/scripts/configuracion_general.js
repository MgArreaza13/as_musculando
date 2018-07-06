/**************************************FORMAS DE PAGO*****************************************/

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





/**************************************COLABORADORES*****************************************/



function EliminarTipoDeColaborador(id_tipo_colaborador) {
	swal({
		  title: '¿Estas Seguro?',
		  text: "¿Estas Seguro de que deseas eliminar este tipo de colaborador?",
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
		    url : '/Configuracion/Tipo/De/Colaboradores/Solicitud/Eliminar/Registro/',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'id':id_tipo_colaborador,
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
					      'Hemos Borrado satisfactoriamente tu tipo de colaborador.',
					      'success'
					    );
		        	location.href ="/Configuracion/";
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al borrar su tipo de colaborador!", "error")
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




function NuevoTipoDeColaborador() {
 swal({
  html: '<h1>Tipo De Colaborador</h1><h3 style="color:blue">Ingrese el tipo de colaborador con que cuenta en sus instalaciones</h3>',
  input: 'text',
  inputPlaceholder: 'Tipo De Colaborador',
  showCancelButton: true,
  inputValidator: (value) => {
  	if (value == '') {
  		return !value && 'Necesitas escribir algo!'
  	}
    else{
    	  	$.ajax({
		    // la URL para la petición
		    url : '/Configuracion/Tipo/De/Colaboradores/Solicitud/Nuevo/Registro/',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'TipoDeColaborador':value,
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
					      'Agregamos Su Tipo de Colaborador satisfactoriamente.',
					      'success'
					    );
		        	location.href ="/Configuracion/";
		    	}
		    	else if (status == 401) {
		    		//todo correcto 
		    		swal(
					      'Error!',
					      'Ya posees un tipo de colaboradoro con ese nombre .',
					      'error'
					    );
		        	
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al cargar su tipo de colaborador!", "error")
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



function EditarTipoDeColaborador(id) {
	$.ajax({
		    // la URL para la petición
		    url : '/Configuracion/Tipo/De/Colaboradores/Get/Registro/',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'id_tipo_colaborador':id,
		    },
		    // el tipo de información que se espera de respuesta
		    dataType : 'json',
		    // código a ejecutar si la petición es satisfactoria;
		    // la respuesta es pasada como argumento a la función
		    success : function(tipo_colaborador) {
		    	if (tipo_colaborador) {
			    	swal({
					  html: '<h1>Editar Tipo De Colaborador</h1><h3 style="color:blue">'+	tipo_colaborador.tipodecolaborador +'</h3>',
					  input: 'text',
					  inputPlaceholder: ''+tipo_colaborador.tipodecolaborador+'',
					  showCancelButton: true,
					  inputValidator: (value) => {
					  	if (value == '') {
					  		return !value && 'Necesitas escribir algo!'
					  	}
					    else{
			    	  	$.ajax({
					    // la URL para la petición
					    url : '/Configuracion/Tipo/De/Colaboradores/Update/Registro/',
					    // la información a enviar
					    // (también es posible utilizar una cadena de datos)
					    data : { 
					    	'id_tipo_colaborador':id,
					    	'nombre_tipo_colaborador':value,
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
								      'Agregamos Su tipo de colaborador correctamente.',
								      'success'
								    );
					        	location.href ="/Configuracion/";
					    	}
					    	else if (status == 401) {
					    		//todo correcto 
					    		swal(
								      'Error!',
								      'Ya posees un tipo de colaborador con esos datos.',
								      'error'
								    );
					        	
					    	}
					    	else{
					    		swal("OOOh!", "Hemos tenido un problema al cargar su registro !", "error")
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
		    		swal("OOOh!", "Hemos tenido un problema al cargar su peticion", "error")
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




/**********************************TIPOS DE EGRESOS******************************************/


function NuevoTipoDeEgreso() {
 swal({
  html: '<h1>Tipo De Egreso</h1><h3 style="color:blue">Ingrese el tipo de Egreso que desea registrar</h3>',
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
		    url : '/Configuracion/Tipo/De/Egreso/Solicitud/Nuevo/Registro/',
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
		        	location.href ="/Configuracion/";
		    	}
		    	else if (status == 401) {
		    		//todo correcto 
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



function EliminarTipoDeEgreso(id_tipo_de_egreso) {
	swal({
		  title: '¿Estas Seguro?',
		  text: "¿Estas Seguro de que deseas eliminar este tipo de Egreso?",
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
		    url : '/Configuracion/Tipo/De/Egreso/Solicitud/Eliminar/Registro/',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'id':id_tipo_de_egreso,
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
					      'Hemos Borrado satisfactoriamente tu tipo de Egreso.',
					      'success'
					    );
		        	location.href ="/Configuracion/";
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al borrar su tipo de Egreso!", "error")
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


function EditarTipoDeEgreso(id) {
	$.ajax({
		    // la URL para la petición
		    url : '/Configuracion/Tipo/De/Egreso/Get/Registro/',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'id_tipo_egreso':id,
		    },
		    // el tipo de información que se espera de respuesta
		    dataType : 'json',
		    // código a ejecutar si la petición es satisfactoria;
		    // la respuesta es pasada como argumento a la función
		    success : function(tipo_egreso) {
		    	if (tipo_egreso) {
			    	swal({
					  html: '<h1>Editar Tipo De Egreso</h1><h3 style="color:blue">'+	tipo_egreso.tipodeEgreso +'</h3>',
					  input: 'text',
					  inputPlaceholder: ''+tipo_egreso.tipodeEgreso+'',
					  showCancelButton: true,
					  inputValidator: (value) => {
					  	if (value == '') {
					  		return !value && 'Necesitas escribir algo!'
					  	}
					    else{
			    	  	$.ajax({
					    // la URL para la petición
					    url : '/Configuracion/Tipo/De/Egreso/Update/Registro/',
					    // la información a enviar
					    // (también es posible utilizar una cadena de datos)
					    data : { 
					    	'id_tipo_egreso':id,
					    	'nombre_tipo_egreso':value,
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
								      'Agregamos Su tipo de Egreso correctamente.',
								      'success'
								    );
					        	location.href ="/Configuracion/";
					    	}
					    	else if (status == 401) {
					    		//todo correcto 
					    		swal(
								      'Error!',
								      'Ya posees un tipo de Egreso con esos datos.',
								      'error'
								    );
					        	
					    	}
					    	else{
					    		swal("OOOh!", "Hemos tenido un problema al cargar su registro !", "error")
					    	}
					    },
					 
					    // código a ejecutar si la petición falla;
					    // son pasados como argumentos a la función
					    // el objeto de la petición en crudo y código de estatus de la petición
					    error : function(xhr, status) {
					        swal("OOOh!", "Hemos tenido un problema con el Servidor, es posible que ya tenga un dato con ese nombre, verifiquelo e intente de nuevo!", "error")
					    },
					 
					    // código a ejecutar sin importar si la petición falló o n
					});
			    }
			  }
			})
		   }
		    	
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al cargar su peticion", "error")
		    	}
		    },
		 
		    // código a ejecutar si la petición falla;
		    // son pasados como argumentos a la función
		    // el objeto de la petición en crudo y código de estatus de la petición
		    error : function(xhr, status) {
		        swal("OOOh!", "Hemos tenido un problema con el Servidor, es posible que ya tenga un dato con ese nombre, verifiquelo e intente de nuevo!", "error")
		    },
		 
		    // código a ejecutar sin importar si la petición falló o n
		});
}





/**********************************TIPOS DE INGRESOS******************************************/


function NuevoTipoDeIngreso() {
 swal({
  html: '<h1>Tipo De Ingreso</h1><h3 style="color:blue">Ingrese el tipo de Ingreso que desea registrar</h3>',
  input: 'text',
  inputPlaceholder: 'Tipo De Ingreso',
  showCancelButton: true,
  inputValidator: (value) => {
  	if (value == '') {
  		return !value && 'Necesitas escribir algo!'
  	}
    else{
    	  	$.ajax({
		    // la URL para la petición
		    url : '/Configuracion/Tipo/De/Ingreso/Solicitud/Nuevo/Registro/',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'TipoDeIngreso':value,
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
					      'Agregamos Su Tipo de Ingreso satisfactoriamente.',
					      'success'
					    );
		        	location.href ="/Configuracion/";
		    	}
		    	else if (status == 401) {
		    		//todo correcto 
		    		swal(
					      'Error!',
					      'Ya posees un tipo de Ingreso con ese nombre .',
					      'error'
					    );
		        	
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al cargar su tipo de Ingreso!", "error")
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



function EliminarTipoDeIngreso(id_tipo_de_ingreso) {
	swal({
		  title: '¿Estas Seguro?',
		  text: "¿Estas Seguro de que deseas eliminar este tipo de Ingreso?",
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
		    url : '/Configuracion/Tipo/De/Ingreso/Solicitud/Eliminar/Registro/',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'id':id_tipo_de_ingreso,
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
					      'Hemos Borrado satisfactoriamente tu tipo de Ingreso.',
					      'success'
					    );
		        	location.href ="/Configuracion/";
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al borrar su tipo de Ingreso!", "error")
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


function EditarTipoDeIngreso(id) {
	$.ajax({
		    // la URL para la petición
		    url : '/Configuracion/Tipo/De/Ingreso/Get/Registro/',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'id_tipo_ingreso':id,
		    },
		    // el tipo de información que se espera de respuesta
		    dataType : 'json',
		    // código a ejecutar si la petición es satisfactoria;
		    // la respuesta es pasada como argumento a la función
		    success : function(tipo_ingreso) {
		    	if (tipo_ingreso) {
			    	swal({
					  html: '<h1>Editar Tipo De Ingreso</h1><h3 style="color:blue">'+	tipo_ingreso.tipodeIngreso +'</h3>',
					  input: 'text',
					  inputPlaceholder: ''+tipo_ingreso.tipodeIngreso+'',
					  showCancelButton: true,
					  inputValidator: (value) => {
					  	if (value == '') {
					  		return !value && 'Necesitas escribir algo!'
					  	}
					    else{
			    	  	$.ajax({
					    // la URL para la petición
					    url : '/Configuracion/Tipo/De/Ingreso/Update/Registro/',
					    // la información a enviar
					    // (también es posible utilizar una cadena de datos)
					    data : { 
					    	'id_tipo_ingreso':id,
					    	'nombre_tipo_ingreso':value,
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
								      'Agregamos Su tipo de Ingreso correctamente.',
								      'success'
								    );
					        	location.href ="/Configuracion/";
					    	}
					    	else if (status == 401) {
					    		//todo correcto 
					    		swal(
								      'Error!',
								      'Ya posees un tipo de Ingreso con esos datos.',
								      'error'
								    );
					        	
					    	}
					    	else{
					    		swal("OOOh!", "Hemos tenido un problema al cargar su registro !", "error")
					    	}
					    },
					 
					    // código a ejecutar si la petición falla;
					    // son pasados como argumentos a la función
					    // el objeto de la petición en crudo y código de estatus de la petición
					    error : function(xhr, status) {
					        swal("OOOh!", "Hemos tenido un problema con el Servidor, es posible que ya tenga un dato con ese nombre, verifiquelo e intente de nuevo!", "error")
					    },
					 
					    // código a ejecutar sin importar si la petición falló o n
					});
			    }
			  }
			})
		   }
		    	
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al cargar su peticion", "error")
		    	}
		    },
		 
		    // código a ejecutar si la petición falla;
		    // son pasados como argumentos a la función
		    // el objeto de la petición en crudo y código de estatus de la petición
		    error : function(xhr, status) {
		        swal("OOOh!", "Hemos tenido un problema con el Servidor, es posible que ya tenga un dato con ese nombre, verifiquelo e intente de nuevo!", "error")
		    },
		 
		    // código a ejecutar sin importar si la petición falló o n
		});
}


