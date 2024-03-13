#!/usr/bin/node

const fs = require('fs');

// Get the file paths from the command line arguments
const [, , inputFile1, inputFile2, outputFile] = process.argv;

// Read the content of the first file
fs.readFile(inputFile1, 'utf8', (err, data1) => {
  if (err) throw err;

  // Read the content of the second file
  fs.readFile(inputFile2, 'utf8', (err, data2) => {
    if (err) throw err;

    // Concatenate the contents of the two files
    const concatenatedContent = data1 + '\n' + data2;

    // Write the concatenated content to the output file
    fs.writeFile(outputFile, concatenatedContent, 'utf8', (err) => {
      if (err) throw err;
      console.log('Files concatenated successfully!');
    });
  });
});
