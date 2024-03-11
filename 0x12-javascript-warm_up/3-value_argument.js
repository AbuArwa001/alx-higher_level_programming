#!/usr/bin/node
const { argv } = require('node:process');
let count = 0;
let value = '';
argv.forEach((element) => {
  if (count === 2) {
    value = element;
  }
  count++;
});
if (count === 2) {
  console.log('No argument');
} else if (count >= 3 && value) {
  console.log(value);
}
