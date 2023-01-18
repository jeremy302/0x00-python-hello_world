#!/usr/bin/node

const fs = require('fs');
const request = require('request');

if (process.argv.length > 3) {
  const [url, path] = process.argv.slice(2);
  request.get(url).pipe(fs.createWriteStream(path));
}
