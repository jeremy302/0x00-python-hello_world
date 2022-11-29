#!/usr/bin/node

module.exports.nbOccurences = (list, searchElement) =>
  list.reduce((count, v) => v === searchElement ? count + 1 : count, 0);
