// Wait for the document to be ready
$(document).ready(() => {
  // Fetch data from the provided URL
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
    // Iterate through each film in the data
    data.results.forEach((film) => {
      // Create a new <li> element with the film title
      const listItem = $('<li></li>').text(film.title);
      // Append the <li> element to the <ul> with id "list_movies"
      $('#list_movies').append(listItem);
    });
  });
});
