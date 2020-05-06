#!/usr/bin/node

/*
Sscript that searches the second biggest integer
in the list of arguments
*/

if (process.argv.length < 4) {
  console.log(0);
  process.exit();
}

const newArray = process.argv.sort((a, b) => (a - b));
console.log(newArray[newArray.length - 2]);
