#!/usr/bin/node

/*
Sscript that searches the second biggest integer
in the list of arguments
*/

let numbers = process.argv;
numbers.shift();
numbers.shift();
numbers = numbers.sort();
if (numbers.length < 2) {
  console.log(0);
} else {
  console.log(numbers[numbers.length - 2]);
}
