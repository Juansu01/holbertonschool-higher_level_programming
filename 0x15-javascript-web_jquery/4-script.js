import $ from 'jquery';

// $('#red_header')
//  .on('click', () => $('header').addClass('red'));

$('#toggle_header').click(function () {
  if ($('header').hasClass('red')) {
    $('header').removeClass('red');
    $('header').addClass('green');
  } else {
    $('header').removeClass('green');
    $('header').addClass('red');
  }
});
