$(document).ready(function () {


    /**
     * SKILL CIRCLES
     * Modified from jquery-circle-progress to use for loop data.
     * Credit: https://github.com/kottenator/jquery-circle-progress
     * Credit: Iterator function from https://stackoverflow.com/questions/34949440/how-to-get-data-attribute-value-of-all-elements-using-jquery
     */
    $('[data-circle]').each(function () {
        $(this).circleProgress({
            value: $(this).attr('data-circle'),
            size: 80,
            fill: {
                gradient: ["#c9c9c9", "#787676"]
            }
        });
    });


    /**
     * ACCORDION
     * Check current state of an accordion target.
     * Hides a visible target and reveals a hidden target.
     * Credit: https://stackoverflow.com/questions/178325/how-do-i-check-if-an-element-is-hidden-in-jquery
     */
    function slide(target) {
        if (target.is(":hidden")) {
            target.slideDown(600);
        } else {
            target.slideUp(600);
        }
    }

    
    /**
     * For each level in the accordion allows a button click to slide a target.
     * Data attribute values allow the association of a button to a target when the template is rendered.
     * Credit: https://stackoverflow.com/questions/31802861/show-hide-elements-by-data-attribute
     * https://www.codeproject.com/Questions/369517/how-to-get-data-attributes-in-jquery
     */
    $('[data-btn]').click(function () {
        let value = $(this).attr('data-btn');
        let target = $('[data-div=' + value + ']');
        $('[data-div]').slideUp(600);
        if (target.is(':hidden')) {} else {}
        slide(target);
    });


});