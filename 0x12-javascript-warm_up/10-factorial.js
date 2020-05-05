#!/usr/bin/node

/*
Sscript that computes and prints a factorial
*/
const a = parseInt(process.argv[2]);

if (isNaN(a)) {
  console.log(1);
  process.exit();
}
function factorial (a) {
  if (a === 1) {
    return (1);
  }
  return factorial(a - 1) * a;
}

console.log(factorial(a));
