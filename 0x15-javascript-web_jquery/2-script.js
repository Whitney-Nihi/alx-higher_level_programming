// Wait for the document to be ready
$(document).ready(() => {
  // Set up a click event listener on the <div> with id "red_header"
  $('#red_header').on('click', () => {
    // Update the text color of the <header> element to red
    $('header').css('color', '#FF0000');
  });
});
