const uri = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const $divCharacter = $('div#character');

$.ajax({
  url: uri,
  dataType: 'json'
}).done((data) => {
  $divCharacter.text(data.name);
});
