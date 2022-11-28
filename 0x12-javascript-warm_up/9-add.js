#!/usr/bin/node
const args = process.argv.slice(2, 4);
const n1 = parseInt(Number(args[0]));
const n2 = parseInt(Number(args[1]));

function add (a, b) {
  return a + b;
}

console.log(add(n1, n2));
