import $ from 'jquery';

$.ajax('https://swapi-api.hbtn.io/api/films/?format=json', // request url
  {
    success: function (data) { // success callback function
      data.results.forEach(movie => {
        $('#list_movies').append(`<li>${movie.title}</li>`);
      });
    }
  });
