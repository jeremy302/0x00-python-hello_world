#!/usr/bin/node

const fs = require('fs');

const [f1, f2, f3] = process.argv.slice(2);
fs.readFile(f1, (_, d1) => {
  fs.readFile(f2, (_, d2) => {
    fs.writeFile(f3, d1 + '\n' + d2 + '\n', () => {});
  });
});
