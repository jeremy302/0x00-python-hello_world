#!/usr/bin/node

module.exports.esrever = (list) => {
  const revlist = [];
  for (const i in list) { revlist[i] = list[list.length - i - 1]; }
  return revlist;
};
