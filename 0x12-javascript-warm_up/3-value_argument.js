#!/usr/bin/node
const argLength = process.argv.reduce((_, __, i) => i) - 1;
if (!argLength) { console.log('No argument'); } else { console.log(process.argv[2]); }
