#!/usr/bin/node
const fs = require('fs');

if (process.argv.length > 3) {
  const [path, str] = process.argv.slice(2);
  fs.writeFile(path, str, e => e && console.log(e));
}
