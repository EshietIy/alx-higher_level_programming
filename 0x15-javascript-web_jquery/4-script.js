$('div#toggle_header').on('click', function  (){
let x = $('header').attr('class');
if (x === 'green') {
$('header').attr('class', 'red');
} else {
$('header').attr('class', 'green');
}
});
