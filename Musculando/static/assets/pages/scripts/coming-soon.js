var ComingSoon = function () {

    return {
        //main function to initiate the module
        init: function () {
            var austDay = new Date();
            austDay = new Date(austDay.getFullYear() + 1, 1 - 1, 26);
            $('#defaultCountdown').countdown({until: austDay});
            $('#year').text(austDay.getFullYear());

            $.backstretch([
		      "http://localhost:8000/static/assets/pages/img/login/l3.jpg",
                "http://localhost:8000/static/assets/pages/img/login/l4.jpg",
                "http://localhost:8000/static/assets/pages/img/login/l5.jpg",
                "http://localhost:8000/static/assets/pages/img/login/l6.jpg",
                
		        ], {
		        fade: 1000,
		        duration: 10000
		   });
        }

    };

}();

jQuery(document).ready(function() {    
   ComingSoon.init(); 
});