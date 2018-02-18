

                function Mostrarformulario () {
                    $('#ContenidoCurso').addClass('hidden');
                    $('#ContenidoCurso').removeClass('animated fadeInLeft');
                    $('#formularioData').removeClass('hidden');
                    $('#formularioData').addClass('animated fadeInRight ');
                }
                function Ocultarformulario () {
                    $('#formularioData').addClass('hidden');
                    $('#formularioData').removeClass('animated fadeInRight ');
                    $('#ContenidoCurso').removeClass('hidden');
                    $('#ContenidoCurso').addClass('animated fadeInLeft');
                }

                function mandarDatosParaCurso(curso){
                  var curso       =  curso;
                  console.log(curso);
                  $.ajax({
                            url: '/Solicitudes/Curso/Perfil/',
                            data: {
                              'curso':curso,

                              },

                          dataType: 'json',
                          success: function (data) {
                                if (data) {
                                alert('Hemos Cargado Sus Datos Satisfactoriamente');
                                    location.reload(); 
                                }
                                else{
                                    console.log('error');
                                }
                          } 
                      });

                }

                function EnviarFormulario(curso) {
                        var nombre      = $('#nombre').val();
                        var apellido    = $('#apellido').val();
                        var cedula      = $('#cedula').val();
                        var correo      = $('#correo').val();
                        var direccion   = $('#direccion').val();
                        var telefono1   = $('#telefono1').val();
                        var telefono2   = $('#telefono2').val();
                        var curso       =  curso;
                        
                         $.ajax({
                            url: '/Solicitudes/Curso/',
                            data: {
                                'nombre':nombre,
                                'apellido':apellido,
                                'cedula':cedula,
                                'correo':correo,
                                'direccion':direccion,
                                'telefono1':telefono1,
                                'telefono2':telefono2,
                                'curso':curso,
                              },

                          dataType: 'json',
                          success: function (data) {
                                if (data) {
                                alert('Hemos Cargado Sus Datos Satisfactoriamente');
                                    location.reload(); 
                                }
                                else{
                                    console.log('error');
                                }
                          } 
                      });

                }
                setInterval(function(){ validarEnviar(); }, 300);
                function validarEnviar(){
                  if ($('#nombre').val() != "" && $('#apellido').val() != "" && $('#cedula').val() != "" && $('#correo').val() != "" && $('#direccion').val() != "" && $('#telefono1').val() != "" && $('#telefono2').val() != ""){
                      $('#EnviarSolicitudCursos').attr("disabled", false);
                  }
                  else{
                     $('#EnviarSolicitudCursos').attr("disabled", true);
                  } 
                }