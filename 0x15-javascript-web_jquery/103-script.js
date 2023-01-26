const translate = () => {
  const lang = $('INPUT#language_code').val();
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=' + lang,
			  data => $('DIV#hello').text(data.hello));
};
$(() => {
  $('INPUT#btn_translate').on('click', translate);
  $('INPUT#language_code').on('keypress', e => {
    if (e.key == 'Enter') { translate(); }
  });
});
