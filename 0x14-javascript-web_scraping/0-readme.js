#!/usr/bin/node
/*
   Write a script that reads and prints
   the content of a file.
 */
const filename = process.argv[2];
const Read = require('fs');
Read.readFile(filename, 'utf8', function (Error, line) {
  if (Error) {
    console.log(Error);
  } else {
    console.log(line);
  }
});
