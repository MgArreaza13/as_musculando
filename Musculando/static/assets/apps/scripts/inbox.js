var AppInbox = function () {

    var content = $('#cuerpoBoxMail');
    var listListing = '';

    var loadInbox = function (el, name) {
        var url = '/api/Mails';
        var title = el.attr('data-title');
        listListing = name;

        App.blockUI({
            target: content,
            overlayColor: 'none',
            animate: true
        });

        toggleButton(el);

        $.ajax({
            cache: false,
            url: url,
            dataType: "json",
            success: function(res) 
            {
                toggleButton(el);

                var contenido = '' ;

                App.unblockUI('.inbox-content');
                for(var i = 0; i<res.length; i++){

                    contenido += '<tr class="unread" data-messageid="'+res[i].id+'">'+
                    '<td class="inbox-small-cells">'+
                        '<label class="mt-checkbox mt-checkbox-single mt-checkbox-outline">'+
                            '<input type="checkbox" class="mail-checkbox" value="1" />'+
                            '<span></span>'+
                        '</label>'+
                    '</td>'+
                    '<td class="inbox-small-cells">'+
                        '<i class="fa fa-star"></i>'+
                    '</td>'+
                    '<td class="view-message hidden-xs">' + res[i].user.username + '</td>'+
                    '<td class="view-message ">'+res[i].Asunto  + ' </td>'+
                    '<td class="view-message inbox-small-cells">'+
                        
                    '</td>'+
                    '<td class="view-message text-right"> '+ res[i].dateCreate  + ' </td>'+
                '</tr>';

                }
                $('.inbox-nav > li.active').removeClass('active');
                el.closest('li').addClass('active');
                $('.inbox-header > h1').text(title);

                

                content.html(contenido);

                if (Layout.fixContentHeight) {
                    Layout.fixContentHeight();
                }
            },
            error: function( ajaxOptions, thrownError)
            {
                toggleButton(el);
            },
            async: false
        });

        // handle group checkbox:
        jQuery('body').on('change', '.mail-group-checkbox', function () {
            var set = jQuery('.mail-checkbox');
            var checked = jQuery(this).is(":checked");
            jQuery(set).each(function () {
                $(this).attr("checked", checked);
            });
        });
    }

    var loadMessage = function (el, name, resetMenu) {
        var url = 'app_inbox_view.html';

        App.blockUI({
            target: content,
            overlayColor: 'none',
            animate: true
        });

        toggleButton(el);

        var message_id = el.parent('tr').attr("data-messageid");  
        
        $.ajax({
            type: "GET",
            cache: false,
            url: url,
            dataType: "html",
            data: {'message_id': message_id},
            success: function(res) 
            {
                App.unblockUI(content);

                toggleButton(el);

                if (resetMenu) {
                    $('.inbox-nav > li.active').removeClass('active');
                }
                $('.inbox-header > h1').text('View Message');

                content.html(res);
                Layout.fixContentHeight();
            },
            error: function( ajaxOptions, thrownError)
            {
                toggleButton(el);
            },
            async: false
        });
    }

    var initWysihtml5 = function () {
        $('.inbox-wysihtml5').wysihtml5({
            "stylesheets": ["../assets/global/plugins/bootstrap-wysihtml5/wysiwyg-color.css"]
        });
    }

    var initFileupload = function () {

        $('#fileupload').fileupload({
            // Uncomment the following to send cross-domain cookies:
            //xhrFields: {withCredentials: true},
            url: '../assets/global/plugins/jquery-file-upload/server/php/',
            autoUpload: true
        });

        // Upload server status check for browsers with CORS support:
        if ($.support.cors) {
            $.ajax({
                url: '../assets/global/plugins/jquery-file-upload/server/php/',
                type: 'HEAD'
            }).fail(function () {
                $('<span class="alert alert-error"/>')
                    .text('Upload server currently unavailable - ' +
                    new Date())
                    .appendTo('#fileupload');
            });
        }
    }

    var loadCompose = function (el) {
        $('#Envidados').addClass('hidden');
        var contenido = $('#Envidados');
        var html =  '<form class="inbox-compose form-horizontal" id="fileupload" action="#" method="POST" enctype="multipart/form-data">'+ 
    '<div class="inbox-compose-btn">'+
        '<button class="btn green">'
            '+<i class="fa fa-check"></i>Send</button>'
        '<button class="btn default inbox-discard-btn">Discard</button>'
        '<button class="btn default">Draft</button>'+
    '</div>'+
    '<div class="inbox-form-group mail-to">'+
        '<label class="control-label">To:</label>'+
        '<div class="controls controls-to">'+
            '<input type="text" class="form-control" name="to">'+
            '<span class="inbox-cc-bcc">'+
                '<span class="inbox-cc"> Cc </span>'+
                '<span class="inbox-bcc"> Bcc </span>'+
            '</span>'
        '</div>'
    '</div>'
    '<div class="inbox-form-group input-cc display-hide">'+
        '<a href="javascript:;" class="close"> </a>'+
        '<label class="control-label">Cc:</label>'+
        '<div class="controls controls-cc">'+
            '<input type="text" name="cc" class="form-control"> </div>'+
    '</div>'+
    '<div class="inbox-form-group input-bcc display-hide">'+
        '<a href="javascript:;" class="close"> </a>'+
        '<label class="control-label">Bcc:</label>'+
        '<div class="controls controls-bcc">'+
            '<input type="text" name="bcc" class="form-control"> </div>'+
    '</div>'+
    '<div class="inbox-form-group">'+
        '<label class="control-label">Subject:</label>'+
        '<div class="controls">'+
            '<input type="text" class="form-control" name="subject"> </div>'+
    '</div>'+
    '<div class="inbox-form-group">'+
        '<textarea class="inbox-editor inbox-wysihtml5 form-control" name="message" rows="12"></textarea>'+
    '</div>'+
    '<div class="inbox-compose-attachment">'+
       
        '<span class="btn green btn-outline fileinput-button">'+
            '<i class="fa fa-plus"></i>'+
            '<span> Add files... </span>'+
            '<input type="file" name="files[]" multiple> </span>'+
        
        '<table role="presentation" class="table table-striped margin-top-10">'+
            '<tbody class="files"> </tbody>'+
       ' </table>'+
    '</div>'+
   
'</form>';
contenido.html(html)  }

    var loadReply = function (el) {
        var messageid = $(el).attr("data-messageid");
        var url = 'app_inbox_reply.html';
        
        App.blockUI({
            target: content,
            overlayColor: 'none',
            animate: true
        });

        toggleButton(el);

        // load the form via ajax
        $.ajax({
            type: "GET",
            cache: false,
            url: url,
            dataType: "html",
            success: function(res) 
            {
                App.unblockUI(content);
                toggleButton(el);

                $('.inbox-nav > li.active').removeClass('active');
                $('.inbox-header > h1').text('Reply');

                content.html(res);
                $('[name="message"]').val($('#reply_email_content_body').html());

                handleCCInput(); // init "CC" input field

                initFileupload();
                initWysihtml5();
                Layout.fixContentHeight();
            },
            error: function(ajaxOptions, thrownError)
            {
                toggleButton(el);
            },
            async: false
        });
    }

    var handleCCInput = function () {
        var the = $('.inbox-compose .mail-to .inbox-cc');
        var input = $('.inbox-compose .input-cc');
        the.hide();
        input.show();
        $('.close', input).click(function () {
            input.hide();
            the.show();
        });
    }

    var handleBCCInput = function () {

        var the = $('.inbox-compose .mail-to .inbox-bcc');
        var input = $('.inbox-compose .input-bcc');
        the.hide();
        input.show();
        $('.close', input).click(function () {
            input.hide();
            the.show();
        });
    }

    var toggleButton = function(el) {
        if (typeof el == 'undefined') {
            return;
        }
        if (el.attr("disabled")) {
            el.attr("disabled", false);
        } else {
            el.attr("disabled", true);
        }
    }

    return {
        //main function to initiate the module
        init: function () {

            // handle compose btn click
            $('.inbox').on('click', '.compose-btn', function () {
                loadCompose($(this));
            });

            // handle discard btn
            $('.inbox').on('click', '.inbox-discard-btn', function(e) {
                e.preventDefault();
                loadInbox($(this), listListing);
            });

            // handle reply and forward button click
            $('.inbox').on('click', '.reply-btn', function () {
                loadReply($(this));
            });

            // handle view message
            $('.inbox').on('click', '.view-message', function () {
                loadMessage($(this));
            });

            // handle inbox listing
            $('.inbox-nav > li > a').click(function () {
                loadInbox($(this), 'inbox');
            });

            //handle compose/reply cc input toggle
            $('.inbox-content').on('click', '.mail-to .inbox-cc', function () {
                handleCCInput();
            });

            //handle compose/reply bcc input toggle
            $('.inbox-content').on('click', '.mail-to .inbox-bcc', function () {
                handleBCCInput();
            });

            //handle loading content based on URL parameter
            if (App.getURLParameter("a") === "view") {
                loadMessage();
            } else if (App.getURLParameter("a") === "compose") {
                loadCompose();
            } else {
               $('.inbox-nav > li:first > a').click();
            }

        }

    };

}();

jQuery(document).ready(function() {
    AppInbox.init();
});