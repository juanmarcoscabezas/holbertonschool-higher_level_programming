#!/usr/bin/node

/*
Sscript that prints the first argument as integer
*/
const number = parseInt(process.argv[2]);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
