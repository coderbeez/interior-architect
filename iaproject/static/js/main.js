$(document).ready(function () {

console.log('test all');



var distance = $('nav').offset().top,
    $window = $(window);

$window.scroll(function() {
    if ( $window.scrollTop() >= distance ) {
        // Your div has reached the top
        console.log("test nav");
        $("[data-nav=navbrand]").show();
    }
});
//https://stackoverflow.com/questions/7543718/test-in-jquery-if-an-element-is-at-the-top-of-screen

    /*$("nav").scroll(function() {
        console.log('test');
        $("[data-nav=navbrand]").show();
       
      });*/

});