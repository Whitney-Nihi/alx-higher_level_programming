// Ensure the DOM is fully loaded
$(document).ready(() => {
  // Add a new item to the list
  $('#add_item').click(() => {
    $('.my_list').append('<li>Item</li>');
  });

  // Remove the last item from the list
  $('#remove_item').click(() => {
    $('.my_list li').last().remove();
  });

  // Clear all items from the list
  $('#clear_list').click(() => {
    $('.my_list').empty();
  });
});
