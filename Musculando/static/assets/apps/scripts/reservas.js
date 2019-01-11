setInterval(function(){
	// console.log($('li.#paso1').hasClass('active'));
	// console.log($('li.#paso2').hasClass('active'));
	// console.log($('li.#paso3').hasClass('active'));
	// console.log($('li.#paso4').hasClass('active'));
	if ($('li#paso2').hasClass('active')== true && $('li#paso2').hasClass('paso3') == false ) {
		$('#botonDeContinuar').addClass('disabled');
	}	
	if ($('li#paso3').hasClass('active')== true && $('li#paso3').hasClass('paso3') == false ) {
		$('#botonDeContinuar').addClass('disabled');
	}	
}, 300)



function selecciondecancha(btn){
	// console.log('seleccionare una cancha')
	$('#cancha').val(btn.name);
	$('li#paso2').addClass('paso3');
	$('.boton2').addClass('disabled');
	$('#botonDeContinuar').removeClass('disabled');
	$('#informacionDeNombre').text($('#Nombre').val());
	$('#informacionDeTelefono').text($('#NumeroDeTelefono').val());
	$('#informacionDeCorreo').text($('#Correo').val());
	$('#dataReserva').text(btn.value);
	$('#CanchaAReservar').text(btn.value);
	$('#informacionDeNombre2').text($('#Nombre').val());
	$('#informacionDeTelefono2').text($('#NumeroDeTelefono').val());
	$('#informacionDeCorreo2').text($('#Correo').val());
	$('#dataReserva2').text(btn.value);
	$('#CanchaAReservar2').text(btn.value);
}

















// ##########################csrftoken#############################
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function continueStep(){
	/*console.log('me dieron click');*/
}

function updateState(id){
	swal({
  title: 'Seleccione el estado al que desea actualizar la reserva',
  input: 'select',
  inputOptions: {
	     'Confirmada': 'Confirmada',
    	 'En Espera': 'En Espera',
    	 'No Aprobada': 'No Aprobada',
	  },
  inputPlaceholder: 'Actualizar Estatus de la reserva',
  showCancelButton: true,
  confirmButtonText: 'Actualizar',
  showLoaderOnConfirm: true,
  inputValidator:(value) => {
  	if(value == ''){
  		return !value && 'Necesitas escribir algo!'
  	}
  } ,
  preConfirm: (newState) => {
  	const data = {'id': id ,'state' : newState}
    return fetch('/Canchas/Reservas/update/state', {
		  method: 'POST', // or 'PUT'
		  body: JSON.stringify(data), // data can be `string` or {object}!
		  headers:{
		    "X-CSRFToken": getCookie("csrftoken"),
        	"Accept": "application/json",
        	"Content-Type": "application/json"
		  }
		})
      .then(response => {
        if (!response.ok) {
          throw new Error(response.statusText)
        }
        return response.json()
      })
      .catch(error => {
        swal.showValidationMessage(
          `Request failed: ${error}`
        )
      })
  },
  allowOutsideClick: () => !swal.isLoading()
}).then((status) => {
  //console.log(status)
  if (status.value.code == 200) {
	swal({
	  type: 'success',
	  title: 'Hemos Actualizado El status perfectamente',
	  showConfirmButton: false,
	  timer: 1500
	})
   $('#status-' + id).html(status.value.state);
  }
})
}







function EnviarReserva(){


swal({
  type:'success',
  title: 'Felicidades',
  text:'Estas Seguro de Concretar esta reserva? si es asi presiona el boton de enviar para proceder a enviarla',
  showCancelButton: true,
  confirmButtonText: 'Enviar',
  showLoaderOnConfirm: true,
  preConfirm: (login) => {
  	const data = { 
  					'nombre': $('#Nombre').val() ,
  					'telefono' : $('#NumeroDeTelefono').val(),
  					'correo' : $('#Correo').val(),
  					'turn': $('#turn').val(),
  					'cancha': $('#cancha').val(),
  					'fecha': $('#fecha').val(),
  				}
   return fetch('/Canchas/Reservas/nueva/web', {
		  method: 'POST', // or 'PUT'
		  body: JSON.stringify(data), // data can be `string` or {object}!
		  headers:{
		    "X-CSRFToken": getCookie("csrftoken"),
        	"Accept": "application/json",
        	"Content-Type": "application/json"
		  }
		})
      .then(response => {
        if (!response.ok) {
          throw new Error(response.statusText)
        }
        return response.json()
      })
      .catch(error => {
        swal.showValidationMessage(
          `Request failed: ${error}`
        )
      })
  },
  allowOutsideClick: () => !swal.isLoading()
}).then((result) => {
	// console.log(result)
  if (result.value.code == 200 ) {
  	// console.log('entre aqui')
    swal(
	  'Gracias',
	  'Gracias por contactarnos, tu reserva se guardo correctamente te avisaremos',
	  'success'
	)
	location.reload(); 
  }
})
}















function DeleteReserva(id) {
	swal({
		  title: '¿Estas Seguro?',
		  text: "¿Estas Seguro de que deseas eliminar esta Reserva?",
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
		    url : '/Canchas/Reservas/delete',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'id_reserva':id,
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
					      'Hemos Borrado satisfactoriamente tu Reserva.',
					      'success'
					    );
		        	$('#reserva-' + id).addClass('hidden');
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al borrar su Reserva!", "error")
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

function ReportarPagoReserva(id_reserva){	
 console.log(id_reserva);
 // console.log(id_monto);
 swal({
  html: '<h2>Añadir Monto</h2><h4 style="color:blue">Ingrese el Monto</h4>',
  input: 'number',
  inputPlaceholder: '$',
  showCancelButton: true,
  inputValidator: (value) => {
  	if (value == '') {
  		return !value && 'Necesitas escribir algo!'
  	}
    else{
    	  	$.ajax({
		    // la URL para la petición
		    url : '/Caja/Nueva/Solicitud/Pago/De/Reserva/',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	// 'PagoDeReserva':value,
		    	'id_reserva':id_reserva,
		    	'id_monto':value,
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
					      'Agregamos Su Monto satisfactoriamente.',
					      'success'
					    );
		        	location.reload(); 
		    	}
		    	else if (status == 401) {
		    		
		    		swal(
					      'Error!',
					      
					      'error'
					    );
		        	
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al cargar el monto!", "error")
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

function configureLoadingScreen(screen){
    $(document)
        .ajaxStart(function () {
            screen.fadeIn();
        })
        .ajaxStop(function () {
            screen.fadeOut();
        });
}
