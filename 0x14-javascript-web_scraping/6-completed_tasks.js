#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  const url = process.argv[2];
  request(url, (e, r, b) => {
    e && console.log(e);
    const map = {};
    const bd = JSON.parse(b);
    for (const item of bd) {
      if (item.completed) {
        if (!map[item.userId]) {
          map[item.userId] = 0;
        }
        map[item.userId]++;
      }
    }
    console.log(map);
  });
}
