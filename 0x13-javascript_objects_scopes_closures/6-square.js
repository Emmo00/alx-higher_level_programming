#!/usr/bin/node
const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    const pixel = c ?? 'X';
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) { row = row.concat(pixel); }
      console.log(row);
    }
  }
}
module.exports = Square;
