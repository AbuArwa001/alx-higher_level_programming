#!/usr/bin/node
// Writes the content to a file specified as the second command-line argument

const request = require('request');
const url = process.argv[2];

request(url, function (_, response, body) {
  console.log('code:', response.statusCode);
});
