// Wait for the document to be ready
$(document).ready(() => {
  // Fetch data from the provided URL
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
    // Update the <div> with id "hello" with the fetched data
    $('#hello').text(data.hello);
  });
});
