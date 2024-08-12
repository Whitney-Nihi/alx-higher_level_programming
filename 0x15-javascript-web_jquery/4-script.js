// Wait for the document to be ready
$(document).ready(() => {
  // Set up a click event listener on the <div> with id "toggle_header"
  $('#toggle_header').on('click', () => {
    // Toggle the class of the <header> element between 'red' and 'green'
    $('header').toggleClass('red green');
  });
});
