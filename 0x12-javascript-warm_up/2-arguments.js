#!/usr/bin/node
const { argv } = require('node:process');
let count = 0;
argv.forEach(element => {
  count++;
});
if (count === 2) {
  console.log('No argument');
} else if (count === 3) {
  console.log('Argument found');
} else if (count > 3) {
  console.log('Arguments found');
}
