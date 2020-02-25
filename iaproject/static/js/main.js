$(document).ready(function () {

    console.log('just navbar js')

    /**
     * NAVBAR ACTIVE
     * Highlight current page as active on navbar.
     */
    function activeNav() {
        let value = $('[data-page]').attr('data-page');
        let target = $('[data-nav=' + value + ']');
        target.addClass('active');
    }

    activeNav();

    /**
     * NAVBAR BRAND
     * Add or remove navbar brand depending on position.
     * Used only on small devices.
     * Credit: Modified https://stackoverflow.com/questions/7543718/test-in-jquery-if-an-element-is-at-the-top-of-screen
     */
    let distance = $('nav').offset().top,
        $window = $(window);

    $window.scroll(function () {
        if ($window.scrollTop() >= distance) {
            $("[data-nav=navbrand]").show();
        } else {
            $("[data-nav=navbrand]").hide();
        }
    });

});