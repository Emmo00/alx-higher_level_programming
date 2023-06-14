#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!w || !h || w <= 0 || h <= 0) return;
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) { row = row.concat('X'); }
      console.log(row);
    }
  }
}
module.exports = Rectangle;
