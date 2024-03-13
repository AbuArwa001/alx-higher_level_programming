#!/usr/bin/node

const list = require('./100-data').list;
const newList = list.map((elemnt, index) => elemnt * index);
console.log(list);
console.log(newList);
