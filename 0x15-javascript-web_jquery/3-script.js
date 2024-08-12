// Wait for the document to be ready
$(document).ready(() => {
  // Set up a click event listener on the <div> with id "red_header"
  $('#red_header').on('click', () => {
    // Add the class "red" to the <header> element
    $('header').addClass('red');
  });
});
