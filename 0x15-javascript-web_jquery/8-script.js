$(() => $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json',
  data => data.results.forEach(m => $('UL#list_movies')
											 .append(`<li>${m.title}</li>`))));
