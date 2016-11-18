$('img').click(function() {
  console.log('data-alt-src value is', $(this).attr('data-alt-src'));
  console.log('src value is', $(this).attr('src'));
});
