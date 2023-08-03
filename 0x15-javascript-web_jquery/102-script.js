const $ = window.$;

$(function loadAfterContent () {
  $('INPUT#btn_translate').on('click', function () {
    const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=';

    const param = $('INPUT#language_code').val();

    $.get(url + param, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
