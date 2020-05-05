#!/usr/bin/node

/*
Sscript that prints a message depending
of the number of arguments passed
*/
let hasParam = false;
process.argv.forEach((val, index) => {
  if (index === 2) {
    hasParam = true;
    console.log(val);
  }
});
if (!hasParam) {
  console.log('No argument');
}
