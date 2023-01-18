#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  const movie = process.argv[2];
  request(`https://swapi-api.hbtn.io/api/films/${movie}/`, (e, r, v) => {
    e && console.log(e);
    const title = JSON.parse(v).title;
    console.log(title);
  });
}
