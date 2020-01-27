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
    else{
        $("[data-nav=navbrand]").hide();
    }
});
//https://stackoverflow.com/questions/7543718/test-in-jquery-if-an-element-is-at-the-top-of-screen

    /*$("nav").scroll(function() {
        console.log('test');
        $("[data-nav=navbrand]").show();
       
      });*/


/**----------------------------------------
    * Accordion
    ----------------------------------------*/

    /**
     * Check current state of an accordion target.
     * Hides a visible target and reveals a hidden target.
     * Credit: https://stackoverflow.com/questions/178325/how-do-i-check-if-an-element-is-hidden-in-jquery
     */
    function slide(target) {
        if (target.is(":hidden")) {
            target.slideDown();
        } else {
            target.slideUp();
        }
    }

    /**
     * For each level in the accordion allows a button click to slide a target.
     * Data attribute values allow the association of a button to a target when the template is rendered.
     * Credit: https://stackoverflow.com/questions/31802861/show-hide-elements-by-data-attribute
     * https://www.codeproject.com/Questions/369517/how-to-get-data-attributes-in-jquery
     */


    
    
     
    $("[data-btn]").click(function () {
        console.log('test slider');
        let value = $(this).attr('data-btn');
        let target = $('[data-div=' + value + ']');
        console.log(value);
        slide(target);
    });



});