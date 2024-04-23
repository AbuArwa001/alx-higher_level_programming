#!/usr/bin/node
// Writes the content to a file specified as the second command-line argument

const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

function writeInFile (filePath, content) {
  try {
    fs.writeFileSync(filePath, content);
  } catch (err) {
    console.error(err);
  }
}

writeInFile(filePath, content);
