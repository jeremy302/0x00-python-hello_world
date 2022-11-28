#!/usr/bin/node
const argLength = process.argv.length - 2;
if (!argLength) { console.log('No argument'); } else { console.log(process.argv[2]); }
