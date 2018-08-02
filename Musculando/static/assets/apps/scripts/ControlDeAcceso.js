function ControlDeAcceso() {
	swal.setDefaults({
			          input: 'text',
			          confirmButtonText: 'Siguiente &rarr;',
			          showCancelButton: true,
			          progressSteps: ['1', '2', '3' ]
			        })
			      //console.log(options);
			        var steps = [
			          {
			           	 title: 'Nombre de Usuario',
						  input: 'text',
						  inputPlaceholder: 'ingrese su nombre de usuario',
			          },
			        {
			            title: 'Password',
			            input: 'password',
						inputPlaceholder: 'ingrese su nombre de usuario',
			          },
			            {
			           	 title: 'Seleccione el Control de Acceso a Marcar ',
						  input: 'select',
						  inputOptions: {
						    'Entrada': 'Entrada',
						    'Salida': 'Salida',
						  },
						  inputPlaceholder: 'Entrada/Salida',
			          },


			          
			        ]

			        swal.queue(steps).then(function (result) {
			        	if (result.value[0] != '' && result.value[1] != '' && result.value[2]){
			        		usuario = result.value[0];
			        		password = result.value[1];
			        		entradaSalida_ = result.value[2];
			        		swal.resetDefaults()
			        	if (result.value[2] == "Entrada") {
						    swal({
						  title: '¿Estas Seguro?',
						  text: "¿Estas Seguro que Deseas Marcar la Entrada?",
						  type: 'warning',
						  showCancelButton: true,
						  confirmButtonColor: '#3085d6',
						  cancelButtonColor: '#d33',
						  confirmButtonText: 'Si, Quiero Marcar!'
						}).then(function (result) {
							//console.log(result)
				           if(result.value){
				           	//console.log('dije que si ');
				    		$.ajax({
			                    url: '/Colaboradores/Solicitud/Para/EntradoSalida/Colaborador',
			                    data: {
			                      'usuario':usuario,
			                      'password': password,
			                      'entradaSalida_':entradaSalida_,
			                  },
			                  dataType: 'json',
			                  success: function (status) {
			                  	if (status = 200) {
			                     swal({
			                        title: 'Hemos Cargado de manera exitosa su pago !',
			                        confirmButtonText: 'Aceptar!'
			                      })
			                     location.reload(); 
			                  		
			                  	}
			                }
			            });
				           	
				           }
				        });
						  }
						else if (result.value[2] == "Salida") {
						    swal({
						  title: '¿Estas Seguro?',
						  text: "¿Estas Seguro de que deseas marcar la Salida?",
						  type: 'warning',
						  showCancelButton: true,
						  confirmButtonColor: '#3085d6',
						  cancelButtonColor: '#d33',
						  confirmButtonText: 'Si, Quiero marcar la Salida!'
						}).then(function (result) {
							console.log(result)
				           if(result.value){
				           	//console.log('dije que si ');
				    		$.ajax({
			                    url: '/Colaboradores/Solicitud/Para/EntradoSalida/Colaborador',
			                    data: {
			                      'usuario':usuario,
			                      'password': password,
			                      'entradaSalida_':entradaSalida_,
			                  },
			                  dataType: 'json',
			                  success: function (status) {
			                     if (status == 200) {
			                     swal({
			                        title: 'Hemos Cargado de manera exitosa su pago !',
			                        confirmButtonText: 'Aceptar!'
			                      })
			                     location.reload(); 
			                  		
			                  	}
			                  	else{
			                  		swal({
			                        title: 'ERROR , No hay Usuario Con Estos Datos !',
			                        confirmButtonText: 'Aceptar!'
			                      })
			                  	}
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
			          swal("OOOh!", "Hemos tenido un problema al verificar sus datos!", "error")
			        })
}