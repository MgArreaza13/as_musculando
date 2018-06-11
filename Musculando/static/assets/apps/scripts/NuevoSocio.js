$('#id_dateInactive_socio').removeAttr("required");
$('#id_nameUser').removeAttr("required");
$('#id_lastName').removeAttr("required");
$('#id_dni').removeAttr("required");
$('#id_movilTlf').removeAttr("required");
$('#id_houseTlf').removeAttr("required");
$('#id_mailUser').removeAttr("required");
$('#id_mailUser').removeAttr("required");
$('#id_obraSocial').removeAttr("required");

function Habilitar() {
$('#id_dateInactive_socio').removeAttr("disabled");
$('#id_nameUser').removeAttr("disabled");
$('#id_lastName').removeAttr("disabled");
$('#id_dni').removeAttr("disabled");
$('#id_movilTlf').removeAttr("disabled");
$('#id_houseTlf').removeAttr("disabled");
$('#id_mailUser').removeAttr("disabled");
$('#id_mailUser').removeAttr("disabled");
$('#id_tipoUser').removeAttr("disabled");
$("#EnviarDatos").removeAttr('disabled');
$('#id_obraSocial').removeAttr("disabled");

$("#Cancelar").removeAttr('disabled');
$('#CambiarAvatar').removeClass('hidden');
$("#Actualizar").attr('disabled', 'disabled');
}

function Desabilitar() {
$('#id_dateInactive_socio').attr('disabled', 'disabled');
$('#id_nameUser').attr('disabled', 'disabled');
$('#id_lastName').attr('disabled', 'disabled');
$('#id_dni').attr('disabled', 'disabled');
$('#id_movilTlf').attr('disabled', 'disabled');
$('#id_houseTlf').attr('disabled', 'disabled');
$('#id_mailUser').attr('disabled', 'disabled');
$('#id_mailUser').attr('disabled', 'disabled');
$('#id_tipoUser').attr('disabled', 'disabled');
$("#EnviarDatos").attr('disabled', 'disabled');
$('#id_obraSocial').attr('disabled', 'disabled');

$("#Cancelar").attr('disabled', 'disabled');
$('#CambiarAvatar').addClass('hidden');

$("#Actualizar").removeAttr('disabled');
}
function ModalSocio() {
	$("#responsive").modal("show");
}
function PlanSeleccionado(id) {
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
		    		$('#SeleccionarPlan').addClass('hidden');
		    		$('#CartadePlan').removeClass('hidden');
		    		$('#TituloPlan').html(plan.nombrePlan);
		    		$('#PrecioPlan').html('<sup class="price-sign">$</sup>'+plan.precioPlan+'</h3>');
		    		$('#TituloPlan').html(plan.nombrePlan);
		    		$('#UserPlan').html(plan.user);
		    		$('#FechaPlan').html(plan.fecha);
		    		$('#IdPlanSeleccionado').val(id);
		    		$("#responsive").modal("hide");	
		    		$('#Enviar').removeClass('btn-warning');
		    		$('#Enviar').addClass('green');
		    		$('#Enviar').text('Guardar');
		    		$('#Enviar').removeAttr("disabled");
		    		

		    	}
		    	else{
		    		$("#responsive").modal("hide");	
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


function configureLoadingScreen(screen){
    $(document)
        .ajaxStart(function () {
            screen.fadeIn();
        })
        .ajaxStop(function () {
            screen.fadeOut();
        });
}
