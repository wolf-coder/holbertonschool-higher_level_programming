#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (h * w > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
