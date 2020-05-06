#!/usr/bin/node

/*
Sscript that searches the second biggest integer
in the list of arguments
*/

if (process.argv.length < 4) {
  console.log(0);
  process.exit();
}

let newArray = process.argv;
newArray.shift();
newArray.shift();
newArray = [...new Set(newArray)];
let first = parseInt(newArray[0]);
let second = newArray[1] === undefined ? first : parseInt(newArray[1]);

if (first < second) {
  const aux = first;
  first = second;
  second = aux;
}

newArray.forEach(val => {
  if (parseInt(val) > first) {
    second = first;
    first = val;
  }
});
console.log(second);
