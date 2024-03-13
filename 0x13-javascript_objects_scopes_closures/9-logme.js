#!/usr/bin/node
exports.logMe = function (item) {
  this.list = this.list || [];
  this.list.push(item);
  console.log(`${this.list.length - 1}: ${item}`);
};
