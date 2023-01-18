#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  const url = process.argv[2];
  request(url, (e, r, b) => {
    if (e) {
      console.log(e);
    } else if (b) {
      const res = JSON.parse(b).results.filter(
        v => v.characters.find(v2 => v2.match(/\/people\/18\/?$/))
      );
      console.log(res.length);
    }
  });
}
