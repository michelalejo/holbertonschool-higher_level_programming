#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let square = '';
    let i = this.height;
    let j = this.width;
    while (i > 0) {
      while (j > 0) {
        square += 'X';
        j--;
      }
      console.log(square);
      i--;
    }
  }
}
module.exports = Rectangle;
