#!/usr/bin/node

/*
Sscript that searches the second biggest integer
in the list of arguments
*/

if (process.argv.length < 4) {
  console.log(0);
  process.exit();
}

let first = process.argv[2];
let second = process.argv[3];

if (first < second) {
  const aux = first;
  first = second;
  second = aux;
}

const newArray = process.argv;
newArray.shift();
newArray.shift();
newArray.forEach(val => {
  if (val > first) {
    second = first;
    first = val;
  }
});
console.log(second);
