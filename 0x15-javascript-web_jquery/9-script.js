import $ from 'jquery';

$.ajax('https://fourtonfish.com/hellosalut/?lang=fr', // request url
  {
    success: function (data) { // success callback function
      $('#hello').html(data.hello);
    }
  });
