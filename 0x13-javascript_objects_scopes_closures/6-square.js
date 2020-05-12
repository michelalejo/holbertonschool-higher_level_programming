#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c !== 'undefined') {
      let square = '';
      let i = this.height;
      let j = this.width;
      while (i > 0) {
        while (j > 0) {
          square += c;
          j--;
        }
        console.log(square);
        i--;
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
