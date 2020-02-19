$(document).ready(function () {

const stripe = Stripe('pk_test_YEXVz6hJlfDMCQfrvKnuAPnG00T43RtZAU');
const sid = $('[data-sid]').attr('data-sid')
console.log(sid)

stripe.redirectToCheckout({
    // Make the id field from the Checkout Session creation API response
    // available to this file, so you can provide it as parameter here
    // instead of the {{CHECKOUT_SESSION_ID}} placeholder.
    sessionId: sid,
  }).then(function (result) {
    // If `redirectToCheckout` fails due to a browser or network
    // error, display the localized error message to your customer
    // using `result.error.message`.
    console.log('error')
  })

console.log('end')



})