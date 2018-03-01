$('#id_nameUser').removeAttr("required");
$('#id_lastName').removeAttr("required");
$('#id_dni').removeAttr("required");
$('#id_movilTlf').removeAttr("required");
$('#id_houseTlf').removeAttr("required");
$('#id_mailUser').removeAttr("required");
$('#id_mailUser').removeAttr("required");

function Habilitar() {
$('#id_nameUser').removeAttr("disabled");
$('#id_lastName').removeAttr("disabled");
$('#id_dni').removeAttr("disabled");
$('#id_movilTlf').removeAttr("disabled");
$('#id_houseTlf').removeAttr("disabled");
$('#id_mailUser').removeAttr("disabled");
$('#id_mailUser').removeAttr("disabled");
$('#id_tipoUser').removeAttr("disabled");
$("#EnviarDatos").removeAttr('disabled');
$("#Cancelar").removeAttr('disabled');
$('#CambiarAvatar').removeClass('hidden');
$("#Actualizar").attr('disabled', 'disabled');
}
function Desabilitar() {
$('#id_nameUser').attr('disabled', 'disabled');
$('#id_lastName').attr('disabled', 'disabled');
$('#id_dni').attr('disabled', 'disabled');
$('#id_movilTlf').attr('disabled', 'disabled');
$('#id_houseTlf').attr('disabled', 'disabled');
$('#id_mailUser').attr('disabled', 'disabled');
$('#id_mailUser').attr('disabled', 'disabled');
$('#id_tipoUser').attr('disabled', 'disabled');
$("#EnviarDatos").attr('disabled', 'disabled');
$("#Cancelar").attr('disabled', 'disabled');
$('#CambiarAvatar').addClass('hidden');

$("#Actualizar").removeAttr('disabled');
}