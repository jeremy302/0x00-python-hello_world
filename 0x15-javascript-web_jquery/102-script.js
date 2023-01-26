$(() => $('INPUT#btn_translate').on('click', () => {
  const lang = $('INPUT#language_code').val();
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=' + lang,
				  data => $('DIV#hello').text(data.hello));
}));
