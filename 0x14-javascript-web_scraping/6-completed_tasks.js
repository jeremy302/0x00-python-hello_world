#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  const url = process.argv[2];
  request(url, (e, r, b) => {
    b = JSON.parse(b);
    e && console.log(e);
    console.log(b.reduce((acc, v) =>
      e.completed ? { ...acc, [e.userId]: (a[e.userId] ?? 0) + 1 } : acc, {}));
  });
}
