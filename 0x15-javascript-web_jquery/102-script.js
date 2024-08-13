// Ensure the DOM is fully loaded
$(document).ready(() => {
  // Attach a click event handler to the translate button
  $('#btn_translate').click(() => {
    // Get the language code from the input field
    const langCode = $('#language_code').val();
    
    // Fetch the translation using the API
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`, (data) => {
      // Update the content of the DIV#hello with the translated "Hello"
      $('#hello').text(data.hello);
    }).fail(() => {
      // Handle errors by displaying a message in the DIV#hello
      $('#hello').text('Error fetching translation');
    });
  });
});
