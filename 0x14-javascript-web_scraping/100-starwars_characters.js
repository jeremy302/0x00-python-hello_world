#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  const movie = process.argv[2];

  request(`https://swapi-api.hbtn.io/api/films/${movie}/`,
    (e, r, b) => {
      e && console.log(e);

      const bd = JSON.parse(b);
      for (const v of bd.characters) {
        request(v, (e, r, b) => {
          const bd2 = JSON.parse(b);
          e && console.log(e);
          console.log(bd2.name);
        });
      }
    });
}
