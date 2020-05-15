#!/usr/bin/node
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $('.result').html(data);
  let i = 0;
  for (i = 0; i < data.count; i++) {
    $('#list_movies').add('<li>' + data.results[i].title + '</li>').appendTo('#list_movies');
  }
});
