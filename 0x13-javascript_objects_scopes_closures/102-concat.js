#!/usr/bin/node

const fs = require('fs');

if (process.argv.length < 5) {
  process.exit();
}

const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];
let text = '';

function readAndWriteFile () {
  text += fs.readFileSync(file1);
  text += fs.readFileSync(file2);
  fs.writeFileSync(file3, text);
}
readAndWriteFile();
