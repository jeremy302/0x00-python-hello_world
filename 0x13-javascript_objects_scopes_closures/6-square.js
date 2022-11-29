#!/usr/bin/node
const OldSquare = require('./5-square.js');

module.exports = class Square extends OldSquare {
  charPrint (c) {
    c = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) { console.log(c.repeat(this.width)); }
  }
};
