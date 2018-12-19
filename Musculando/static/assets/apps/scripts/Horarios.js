setInterval(function(){ $('.clockpicker').clockpicker({
  placement: 'top',
  donetext: 'GUARDAR'
function  EditarTipoHorario(id) {
	        $.ajax({
		    
		    url : 'http://localhost:8000/Configuracion/Tipo/De/Horario/Get/Registro/',
		  	method: 'GET',
		    data : { 
		    	'id_tipo_de_horario':id,
		    },
		    
		    dataType : 'json',
		    
		    success : function(tipo_horario) {

		    	if (tipo_horario) {

			    	swal({
					  html: '<div class="input-group clockpicker"><label >Hora de Inicio</label><input readonly="True" type="text" name="TimeTurnStart" placeholder="Hora Inicial" class="form-control" autocomplete="off" step="1" required autofocus/>'+
                '</div>'+                  
                    '<br>'+
                    '<br>'+
               '<div class="input-group clockpicker">'+
                        '<label >Hora de Cierre</label>'+
                            '<input readonly="True" type="text" name="TimeTurnEnd" placeholder="Hora de Cierre" class="form-control" autocomplete="off" '+
                                       'step="1" required autofocus/>'+

                '</div>',
					  input: 'text',
					  inputPlaceholder: ''+tipo_horario.tipo_horario+'',
					  showCancelButton: true,
					  inputValidator: (value) => {
					  	if (value == '') {
					  		return !value && 'Necesitas escribir algo!'
					  	}
					    else{
			    	  	$.ajax({
					    
					    url : 'http://localhost:8000/Configuracion/Tipo/De/Horario/Update/Registro/',
					    
					    data : { 
					    	'id_tipo_de_horario':id,
					    	'nametipoHorario':value,
					    	'hora_inicial':value,
					    	'hora_de_cierre':value
					    },
					    
					    dataType : 'json',
					    
					    success : function(status) {
					    	//console.log(status)
					    	if (status == 200) {
					    		//todo correcto 
					    		swal(
								      'Felicidades!',
								      'Agregamos Su tipo de Egreso satisfactoriamente.',
								      'success'
								    );
					        	location.href ="/configuracion/";
					    	}
					    	else if (status == 401) {
					    		//todo correcto 
					    		swal(
								      'Error!',
								      'Ya posees un tipo con ese nombre .',
								      'error'
								    );
					        	
					    	}
					    	else{
					    		swal("OOOh!", "Hemos tenido un problema al cargar su petición!", "error")
					    	}
					    },
					 
					    
					    error : function(xhr, status) {
					        swal("OOOh!", "Hemos tenido un problema con el Servidor!", "error")
					    },
					 
					    
					});
			    }
			  }
			})
		   }
		    },
		 		 
		});
           }
           , 300);