function Descuento(id_socio) {
    var myArrayOfThings;
	$.ajax({
	    // la URL para la petición
	    url : '/Configuracion/Porcentaje/Get',
	    dataType : 'json',
	    // código a ejecutar si la petición es satisfactoria;
	    // la respuesta es pasada como argumento a la función
	    success : function(data) {
		    	
		  myArrayOfThings  = data
		  var options = {};
		  $.map(myArrayOfThings,function(o,query) {options[o.porcentajesop] = o.porcentajesop;});
      	  swal({
          title: 'Descuentos',
          text: "Selecciona el porcentaje del descuento",
          input: 'select',
          inputOptions: options,
          confirmButtonText: 'OK',
          showCancelButton: true,
          
        }).then(function (result) {
          porcentajesop = result.value;
              
               swal.resetDefaults()
                $.ajax({
                    url: '/Socios/Nuevo/Descuento',
                    data: {
                      'porcentajesop':porcentajesop,
                      'id_socio':id_socio,
                  },
                  dataType: 'json',
                  success: function (status) {
                     swal(
                'Felicidades!',
                'Hemos registrado este descuento al Socio Seleccionado!',
                'success'
              );
                     location.reload(); 
                }
            });

        }, function () {
          swal.resetDefaults()
        })
    }
        });
  }     

        