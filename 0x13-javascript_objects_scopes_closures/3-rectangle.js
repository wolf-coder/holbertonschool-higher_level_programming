#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (h * w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = '';
    for (let i = 0; i < this.height; i++) {
      str = '';
      for (let j = 0; j < this.width; j++) {
        str += 'X';
      }
      console.log(str);
    }
  }
}
module.exports = Rectangle;
