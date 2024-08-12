// Wait for the document to be ready
$(document).ready(() => {
  // Fetch data from the provided URL
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data) => {
    // Get the character name from the fetched data
    const characterName = data.name;
    // Update the content of the <div> with id "character"
    $('#character').text(characterName);
  });
});
