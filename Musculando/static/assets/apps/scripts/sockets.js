var ws_scheme_dispatch = window.location.protocol == "https:" ? "wss" : "ws";
var ws_path_dispatch = ws_scheme_dispatch + '://' + window.location.host;

dispatch_socket = new WebSocket(ws_path_dispatch);

dispatch_socket.onmessage = function(message) {
        
        var data = JSON.parse(message.data);
       // var miguel_message = message.data.reply_channel
        // if action is started, add new item to table
       // if (data.action == "started") {
           // task_status.append("Mensaje recibido");
        //}
        // if action is completed, just update the status
        //else if (data.action == "completed"){
            console.log(data)
            if (data.action == 'liquidacion') {
                Push.create("Musculando | Colaboradores!", {
                body: "Hemos imputado satisfactoriamente a todos los colaboradores su deuda en su cuenta corriente",
                icon: '/static/assets/pages/img/logo2.png',
                timeout: 400000000000000,
                onClick: function () {
                    window.focus();
                    this.close();
                }
            });
                //location.href ="/";
            }
            if (data.action == 'presentimo') {
                Push.create("Musculando | Presentimo!", {
                body: "Hemos imputado satisfactoriamente a todos los colaboradores el monto de Presentimo",
                icon: '/static/assets/pages/img/logo2.png',
                timeout: 400000000000000,
                onClick: function () {
                    window.focus();
                    this.close();
                }
            });
                //location.href ="/";
            }

            if (data.action == 'socio_creado') {
                Push.create("Musculando | Nuevo Socio!", {
                body: "Hemos creado satisfactoriamente a un nuevo socio",
                icon: '/static/assets/pages/img/logo2.png',
                timeout: 400000000000000,
                onClick: function () {
                    window.focus();
                    this.close();
                }
            });
                //location.href ="/";
            }
       // }
    }

if (dispatch_socket.readyState == WebSocket.OPEN) dispatch_socket.onopen();

        

        