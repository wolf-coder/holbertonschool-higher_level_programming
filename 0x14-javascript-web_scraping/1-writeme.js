#!/usr/bin/node
/*
  Write a script that writes a string to a file.
*/
const Read = require('fs');
const filename = process.argv[2];
const FileContent = process.argv[3];

Read.writeFile(filename, FileContent, function (Error) {
  if (Error) {
    console.log(Error);
  }
});
