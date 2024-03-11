#!/usr/bin/node
const { argv } = require('node:process');
let count = 0;
let value = '';
argv.forEach((element) => {
  value = element;
  if (count >= 3) {
    console.log(`${element}`);
  }
  count++;
});
if (count === 2) {
  console.log('No argument');
} else if (count === 3 && value) {
  console.log(value);
} else if (count > 3) {
  console.log('Arguments found');
}
