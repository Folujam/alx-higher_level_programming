#!/usr/bin/node
/* class that defines a Rectangle */

export default class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
        const emptyObject = {};
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
