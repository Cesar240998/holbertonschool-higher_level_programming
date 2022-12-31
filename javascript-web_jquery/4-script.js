$(function ($) {
  $('DIV#toggle_header').on('click', function (event) {
    $('header').toggleClass('green').addClass('red');
  });
});
