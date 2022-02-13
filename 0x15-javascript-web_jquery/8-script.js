$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
let result = data.results;
for (i = 0; i < result.length; i++){
$('ul#list_movies').append('<li>' + result[i].title) + '<\li>';   
}
});
