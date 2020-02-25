$(document).ready(function () {

  const stripe = Stripe('pk_test_YEXVz6hJlfDMCQfrvKnuAPnG00T43RtZAU');
  const sid = $('[data-sid]').attr('data-sid');

  /**
   * Make the id field from the Checkout Session creation API response available to this file.
   * Credit: https://stripe.com/docs/payments/checkout/one-time
   */
  stripe.redirectToCheckout({
    sessionId: sid,
  });

});