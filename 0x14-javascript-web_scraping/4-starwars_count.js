#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url, function (error, response, body) {
  if (error) return console.error(error);

  try {
    const films = JSON.parse(body).results;
    const wedgeAntillesId = '18'; // Assuming '18' is the ID for Wedge Antilles
    const count = films.reduce((acc, film) => {
      const hasWedge = film.characters.some(characterUrl => characterUrl.endsWith(`/${wedgeAntillesId}/`));
      return acc + (hasWedge ? 1 : 0);
    }, 0);

    console.log(count);
  } catch (e) {
    console.error(e);
  }
});
