// Ensure the DOM is fully loaded
$(document).ready(() => {
  // Function to fetch and display the translation
  const fetchTranslation = () => {
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
  };

  // Attach click event handler to the translate button
  $('#btn_translate').click(fetchTranslation);

  // Attach keypress event handler to the input field
  $('#language_code').keypress((event) => {
    if (event.which === 13) { // Check if ENTER key is pressed
      fetchTranslation();
    }
  });
});
