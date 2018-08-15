setInterval(function () {
	if($('#SeleccionarFiltro').val()=='Anual'){
		$('#Anual').removeClass('hidden');
		$('#Mensual').addClass('hidden');
		$('#Dia').addClass('hidden');
		$('#FilterByEgreso').addClass('hidden');
	}
	else if ($('#SeleccionarFiltro').val()=='Mensual') {
		$('#Anual').addClass('hidden');
		$('#Mensual').removeClass('hidden');
		$('#Dia').addClass('hidden');
		$('#FilterByEgreso').addClass('hidden');

	}
	else if ($('#SeleccionarFiltro').val()=='Fecha') {
		$('#Anual').addClass('hidden');
		$('#Mensual').addClass('hidden');
		$('#FilterByEgreso').addClass('hidden');
		$('#Dia').removeClass('hidden');

	}
	else if ($('#SeleccionarFiltro').val()=='TipoEgreso') {
		$('#Anual').addClass('hidden');
		$('#Mensual').addClass('hidden');
		$('#Dia').addClass('hidden');
		$('#FilterByEgreso').removeClass('hidden');

	}
	else if ($('#SeleccionarFiltro').val()=='Seleccionar') {
		$('#Anual').addClass('hidden');
		$('#Mensual').addClass('hidden');
		$('#Dia').addClass('hidden');
		$('#FilterByEgreso').addClass('hidden');
		$('#ResultadosDeBusquedacontainer').addClass('hidden');
		$('#ResultadosDeBusqueda').addClass('hidden');
		$('#ContainerGeneral').removeClass('hidden');
	}

}, 300);


function BusquedaAnual() {
	year = $('#QueryAnual').val();
	$('#ResultadosDeBusquedacontainer').removeClass('hidden');
	$('#ResultadosDeBusqueda').removeClass('hidden');
	$('#ContainerGeneral').addClass('hidden');

	$.ajax({
		    // la URL para la petición
		    url : '/Caja/Ingresos/QueryAnual/',
		    data : { 
		    	'year':year,
		    },
		    dataType : 'json',
		    
		    success : function(data) {
		    	if (data) {
		    		var htmlEgresos = "";
		    		var htmlIngreso = "";
		    		var ingresosTotal_ = 0;
		    		var egresosTotal_ = 0;
		    		for (var i = 0 ; i < data.length; i++) {
		    			// ingresos , egresos 
		    			if(data[i].model == "Caja.tb_egreso"){
		    				
		    				// egresos

		    				htmlEgresos += '<tr class="odd gradeX">'+
		                      ' <td>'+
		                        ' <label class="mt-checkbox mt-checkbox-single mt-checkbox-outline">'+
		                            '<input type="checkbox" class="checkboxes" value="1" />'+
		                              '<span></span>'+
		                             '</label>'+
		                       '</td>'+
		                       
		                      ' <td> '+data[i].fields.descripcion+'</td>'+
		                       '<td><span class="label label-danger"> $'+data[i].fields.monto+' </span></td>'+
		                      
		                      ' <td> '+data[i].fields.dateCreate+' </td>'+
		                                                
		                       '</tr>';
		                       egresosTotal_ += parseFloat(data[i].fields.monto);
		    			}
		    			else{
		    				htmlIngreso += '<tr class="odd gradeX">'+
		                      ' <td>'+
		                        ' <label class="mt-checkbox mt-checkbox-single mt-checkbox-outline">'+
		                            '<input type="checkbox" class="checkboxes" value="1" />'+
		                              '<span></span>'+
		                             '</label>'+
		                       '</td>'+
		                       
		                      ' <td> '+data[i].fields.descripcion+'</td>'+
		                       '<td><span class="label label-success"> $'+data[i].fields.monto+' </span></td>'+
		                      
		                      ' <td> '+data[i].fields.dateCreate+' </td>'+
		                                                
		                       '</tr>';
		                       ingresosTotal_ += parseFloat(data[i].fields.monto);
		    			}
		    		}
		    		
		    			
		    			$('#CuerpoEgreso').html(htmlEgresos);
		    			$('#CuerpoIngreso').html(htmlIngreso);
		    			$('#IngresosQueryResult').html(ingresosTotal_);
		    			$('#EgresoQueryResult').html(egresosTotal_);
		    			

		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema con su busqueda", "error")
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

function BusquedaMensual() {
	year = $('#YearOfMonth').val();
	month = $('#Month').val();
	$('#ResultadosDeBusquedacontainer').removeClass('hidden');
	$('#ResultadosDeBusqueda').removeClass('hidden');
	$('#ContainerGeneral').addClass('hidden');
	$.ajax({
		    // la URL para la petición
		    url : '/Caja/Ingresos/QueryMensual/',
		    data : { 
		    	'year':year,
		    	'month':month
		    },
		    dataType : 'json',
		    
		    success : function(data) {
		    	if (data) {
		    		var htmlEgresos = "";
		    		var htmlIngreso = "";
		    		var ingresosTotal_ = 0;
		    		var egresosTotal_ = 0;
		    		for (var i = 0 ; i < data.length; i++) {
		    			// ingresos , egresos 
		    			if(data[i].model == "Caja.tb_egreso"){
		    				
		    				// egresos

		    				htmlEgresos += '<tr class="odd gradeX">'+
		                      ' <td>'+
		                        ' <label class="mt-checkbox mt-checkbox-single mt-checkbox-outline">'+
		                            '<input type="checkbox" class="checkboxes" value="1" />'+
		                              '<span></span>'+
		                             '</label>'+
		                       '</td>'+
		                       
		                      ' <td> '+data[i].fields.descripcion+'</td>'+
		                       '<td><span class="label label-danger"> $'+data[i].fields.monto+' </span></td>'+
		                      
		                      ' <td> '+data[i].fields.dateCreate+' </td>'+
		                                                
		                       '</tr>';
		                       egresosTotal_ += parseFloat(data[i].fields.monto);
		    			}
		    			else{
		    				htmlIngreso += '<tr class="odd gradeX">'+
		                      ' <td>'+
		                        ' <label class="mt-checkbox mt-checkbox-single mt-checkbox-outline">'+
		                            '<input type="checkbox" class="checkboxes" value="1" />'+
		                              '<span></span>'+
		                             '</label>'+
		                       '</td>'+
		                       
		                      ' <td> '+data[i].fields.descripcion+'</td>'+
		                       '<td><span class="label label-success"> $'+data[i].fields.monto+' </span></td>'+
		                      
		                      ' <td> '+data[i].fields.dateCreate+' </td>'+
		                                                
		                       '</tr>';
		                       ingresosTotal_ += parseFloat(data[i].fields.monto);
		    			}
		    		}
		    		
		    			
		    			$('#CuerpoEgreso').html(htmlEgresos);
		    			$('#CuerpoIngreso').html(htmlIngreso);
		    			$('#IngresosQueryResult').html(ingresosTotal_);
		    			$('#EgresoQueryResult').html(egresosTotal_);
		    			

		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema con su peticion", "error")
		    	}
		    },
		 
		    // código a ejecutar si la petición falla;
		    // son pasados como argumentos a la función
		    // el objeto de la petición en crudo y código de estatus de la petición
		    error : function(xhr, status) {
		        swal("OOOh!", "Hemos tenido un problema con su busqueda!", "error")
		    },
		 
		    // código a ejecutar sin importar si la petición falló o n
		});
}

function BusquedaFecha() {
	dia = $('#FechaSeleccionada').val();
	$('#ResultadosDeBusquedacontainer').removeClass('hidden');
	$('#ResultadosDeBusqueda').removeClass('hidden');
	$('#ContainerGeneral').addClass('hidden');
	$.ajax({
		    // la URL para la petición
		    url : '/Caja/Ingresos/QueryDia/',
		    data : { 
		    	'dia':dia,
		    },
		    dataType : 'json',
		    
		    success : function(data) {
		    	if (data) {
		    		var htmlEgresos = "";
		    		var htmlIngreso = "";
		    		var ingresosTotal_ = 0;
		    		var egresosTotal_ = 0;
		    		for (var i = 0 ; i < data.length; i++) {
		    			// ingresos , egresos 
		    			if(data[i].model == "Caja.tb_egreso"){
		    				
		    				// egresos

		    				htmlEgresos += '<tr class="odd gradeX">'+
		                      ' <td>'+
		                        ' <label class="mt-checkbox mt-checkbox-single mt-checkbox-outline">'+
		                            '<input type="checkbox" class="checkboxes" value="1" />'+
		                              '<span></span>'+
		                             '</label>'+
		                       '</td>'+
		                       
		                      ' <td> '+data[i].fields.descripcion+'</td>'+
		                       '<td><span class="label label-danger"> $'+data[i].fields.monto+' </span></td>'+
		                      
		                      ' <td> '+data[i].fields.dateCreate+' </td>'+
		                                                
		                       '</tr>';
		                       egresosTotal_ += parseFloat(data[i].fields.monto);
		    			}
		    			else{
		    				htmlIngreso += '<tr class="odd gradeX">'+
		                      ' <td>'+
		                        ' <label class="mt-checkbox mt-checkbox-single mt-checkbox-outline">'+
		                            '<input type="checkbox" class="checkboxes" value="1" />'+
		                              '<span></span>'+
		                             '</label>'+
		                       '</td>'+
		                       
		                      ' <td> '+data[i].fields.descripcion+'</td>'+
		                       '<td><span class="label label-success"> $'+data[i].fields.monto+' </span></td>'+
		                      
		                      ' <td> '+data[i].fields.dateCreate+' </td>'+
		                                                
		                       '</tr>';
		                       ingresosTotal_ += parseFloat(data[i].fields.monto);
		    			}
		    		}
		    		
		    			
		    			$('#CuerpoEgreso').html(htmlEgresos);
		    			$('#CuerpoIngreso').html(htmlIngreso);
		    			$('#IngresosQueryResult').html(ingresosTotal_);
		    			$('#EgresoQueryResult').html(egresosTotal_);
		    			

		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema con su busqueda", "error")
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


function BusquedaPorTipoEgreso() {
	year = $('#tipo_egreso_Year').val();
	month = $('#tipo_egreso_Month').val();
	tipo_egreso = $('#Tipo_Egreso').val();
	$('#ResultadosDeBusquedacontainer').removeClass('hidden');
	$('#ResultadosDeBusqueda').removeClass('hidden');
	$('#ContainerGeneral').addClass('hidden');
	$.ajax({
		    // la URL para la petición
		    url : '/Caja/Ingresos/QueryTipoEgreso/',
		    data : { 
		    	'year':year,
		    	'month':month,
		    	'tipo_egreso':tipo_egreso,
		    },
		    dataType : 'json',
		    
		    success : function(data) {
		    	if (data) {
		    		var htmlEgresos = "";
		    		var htmlIngreso = "";
		    		var ingresosTotal_ = 0;
		    		var egresosTotal_ = 0;
		    		for (var i = 0 ; i < data.length; i++) {
		    			// ingresos , egresos 
		    			if(data[i].model == "Caja.tb_egreso"){
		    				
		    				// egresos

		    				htmlEgresos += '<tr class="odd gradeX">'+
		                      ' <td>'+
		                        ' <label class="mt-checkbox mt-checkbox-single mt-checkbox-outline">'+
		                            '<input type="checkbox" class="checkboxes" value="1" />'+
		                              '<span></span>'+
		                             '</label>'+
		                       '</td>'+
		                       
		                      ' <td> '+data[i].fields.descripcion+'</td>'+
		                       '<td><span class="label label-danger"> $'+data[i].fields.monto+' </span></td>'+
		                      
		                      ' <td> '+data[i].fields.dateCreate+' </td>'+
		                                                
		                       '</tr>';
		                       egresosTotal_ += parseFloat(data[i].fields.monto);
		    			}
		    			else{
		    				htmlIngreso += '<tr class="odd gradeX">'+
		                      ' <td>'+
		                        ' <label class="mt-checkbox mt-checkbox-single mt-checkbox-outline">'+
		                            '<input type="checkbox" class="checkboxes" value="1" />'+
		                              '<span></span>'+
		                             '</label>'+
		                       '</td>'+
		                       
		                      ' <td> '+data[i].fields.descripcion+'</td>'+
		                       '<td><span class="label label-success"> $'+data[i].fields.monto+' </span></td>'+
		                      
		                      ' <td> '+data[i].fields.dateCreate+' </td>'+
		                                                
		                       '</tr>';
		                       ingresosTotal_ += parseFloat(data[i].fields.monto);
		    			}
		    		}
		    		
		    			
		    			$('#CuerpoEgreso').html(htmlEgresos);
		    			$('#CuerpoIngreso').html(htmlIngreso);
		    			$('#IngresosQueryResult').html(ingresosTotal_);
		    			$('#EgresoQueryResult').html(egresosTotal_);
		    			

		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema con su busqueda", "error")
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

