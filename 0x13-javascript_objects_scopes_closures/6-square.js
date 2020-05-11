#!/usr/bin/node

const Square = require('./5-square');

class SquareC extends Square {
  charPrint (c) {
    const char = c === undefined ? 'X' : c;

    for (let i = 0; i < this.height; i++) {
      let rectangleString = '';
      for (let j = 0; j < this.width; j++) {
        rectangleString += char;
      }
      console.log(rectangleString);
    }
  }
}

module.exports = SquareC;
