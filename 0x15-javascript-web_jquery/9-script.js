$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
let hello = data['hello'];
$('div#hello').html(hello);
});
