#!/usr/bin/node

const fs = require('fs');

if (process.argv.length > 2) {
  fs.readFile(process.argv[2], (e, v) => {
    console.log(e || v.toString('utf-8'));
  });
}
