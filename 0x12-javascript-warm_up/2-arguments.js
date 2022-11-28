#!/usr/bin/node
const argLength = process.argv.length - 2;
if (!argLength) { console.log('No argument'); } else if (argLength === 1) { console.log('Argument found'); } else { console.log('Arguments found'); }
