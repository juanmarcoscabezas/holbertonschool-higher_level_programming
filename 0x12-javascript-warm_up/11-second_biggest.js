#!/usr/bin/node

/*
Sscript that searches the second biggest integer
in the list of arguments
*/

let first = 0;
let second = 0;
process.argv.forEach(val => {
  if (val > first) {
    second = first;
    first = val;
  }
});
console.log(second);
