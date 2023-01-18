#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  const url = process.argv[2];
  request(url, (e, r) => console.log(`code: ${r.statusCode}`));
}
