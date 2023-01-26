$(() => $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr',
  data => console.log(data) && $('DIV#hello').text(data.hello)));
