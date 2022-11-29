#!/usr/bin/node

let logIndex = 0;
module.exports.logMe = (item) => {
  console.log(`${logIndex++}: ${item}`);
};
