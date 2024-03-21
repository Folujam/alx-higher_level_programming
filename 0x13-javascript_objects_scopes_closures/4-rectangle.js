#!/usr/bin/node
/* class that defines a Rectangle */

module.exports = class Rectangle {
    constructor (w, h) {
      if (w <= 0 || h <= 0) {
        this.width = null;
        this.height = null;
      } else {
        this.width = w;
        this.height = h;
      }
    }
    print () {
      for (let i = 0; i < this.height; i++){
        console.log('X'.repeat(this.width));
      }
    }
    rotate () {
        let temp = this.width;
        this.width = this.height;
        this.height = temp;
        return [this.width, this.width];
    }
    double () {
      const mw = this.width * 2;
      const mh = this.height * 2;
      return [mw, mh];
    }
};