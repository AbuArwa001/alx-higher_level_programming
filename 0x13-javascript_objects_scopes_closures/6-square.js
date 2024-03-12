#!/usr/bin/node

const Square0 = require('./5-square');

class Square extends Square0 {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write(c);
        }
        console.log();
      }
    }
  }
}

module.exports = Square;
