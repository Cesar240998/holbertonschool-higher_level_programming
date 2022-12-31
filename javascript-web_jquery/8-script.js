$(function ($) {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, textStatus) {
    for (const item of data.results) {
      $('UL#list_movies').append($('<li></li>').text(item.title));
    }
  });
});
