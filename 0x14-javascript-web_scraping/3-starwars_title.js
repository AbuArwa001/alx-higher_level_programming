#!/usr/bin/node
// Writes the content to a file specified as the second command-line argument

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, function (_, response, body) {
  console.log(JSON.parse(body).title);
});
