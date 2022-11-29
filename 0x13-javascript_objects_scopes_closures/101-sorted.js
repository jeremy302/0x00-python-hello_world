#!/usr/bin/node

const dict = require('./101-data.js').dict;
const tally = {};

for (const key in dict) {
  if (dict[key] in tally) { tally[dict[key]].push(key); } else { tally[dict[key]] = [key]; }
}
console.log(tally);
