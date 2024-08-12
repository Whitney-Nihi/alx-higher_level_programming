// Wait for the document to be ready
$(document).ready(() => {
  // Set up a click event listener on the <div> with id "update_header"
  $('#update_header').on('click', () => {
    // Update the text of the <header> element
    $('header').text('New Header!!!');
  });
});
