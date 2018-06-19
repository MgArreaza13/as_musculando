$('#id_proveedor').removeAttr("required");
$('#id_colaborador').removeAttr("required");


setInterval(function () {
		
		if ( $("#id_tipoDeEgreso option:selected").html() == 'Pago Colaboradores') {
			$('#ColaboradorInput').removeClass('hidden');
			$('#ProveedorInput').addClass('hidden');
			$('#id_proveedor').val("");
		}
		else if( $("#id_tipoDeEgreso option:selected").html() == 'Pago Proveedores'){
			$('#ColaboradorInput').addClass('hidden');
			$('#id_colaborador').val("");
			$('#ProveedorInput').removeClass('hidden')
		}
		else{
			$('#ColaboradorInput').addClass('hidden');
			$('#ProveedorInput').addClass('hidden');
			$('#id_colaborador').val("");
			$('#id_proveedor').val("");
		}

	 }, 300);