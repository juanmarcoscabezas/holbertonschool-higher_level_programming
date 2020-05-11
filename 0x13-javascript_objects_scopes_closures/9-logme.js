#!/usr/bin/node

const calls = [];
let pos = 0;

function logMe (item) {
  calls.push(item);
  console.log(pos + ': ' + calls[pos]);
  pos++;
}

module.exports.logMe = logMe;
