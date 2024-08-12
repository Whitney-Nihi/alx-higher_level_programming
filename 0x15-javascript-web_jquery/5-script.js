// Wait for the document to be ready
$(document).ready(() => {
  // Set up a click event listener on the <div> with id "add_item"
  $('#add_item').on('click', () => {
    // Append a new <li> element with text 'Item' to the <ul> with class 'my_list'
    $('.my_list').append('<li>Item</li>');
  });
});
