#!/usr/bin/node
const nums = process.argv.slice(2).map(arg => parseInt(Number(arg)));

if (nums.length <= 1) { console.log('0'); } else { console.log(nums.sort((a, b) => b - a)[1].toString()); }
