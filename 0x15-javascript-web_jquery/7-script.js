import $ from 'jquery';

$.ajax('https://swapi-api.hbtn.io/api/people/5/?format=json', // request url
  {
    success: function (data) { // success callback function
      $('#character').html(data.name);
    }
  });
