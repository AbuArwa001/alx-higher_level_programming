#!/usr/bin/node
// script that prints the number of movies where the
// character “Wedge Antilles” is present

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url, function (_, response, body) {
  let count = 0;
  const dict = JSON.parse(body);
  const obj = dict.results;
  for (let index = 0; index < obj.length; index++) {
    const oneObj = obj[index];
    if (oneObj.characters) {
      const characters = oneObj.characters;
      for (let actor = 0; actor < characters.length; actor++) {
        if (characters[actor].includes('18')) {
          count++;
        }
      }
    }
  }
  console.log(count);
});
