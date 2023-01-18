#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  const url = process.argv[2];
  request(url, (e, r, b) => {
    if (e) {
      console.log(e);
    } else if (b){
      b = JSON.parse(b);
      console.log(b.results.reduce((acc, v) =>
        acc + v.characters.some(c => c.endsWith('/people/18')), 0));
    }
  });
}
