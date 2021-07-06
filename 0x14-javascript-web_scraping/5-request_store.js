#!/usr/bin/node
/*
  Write a script that gets the contents of a webpage and stores it in a file.
*/
const Read = require('fs');
const request = require('request');
const Url = process.argv[2];
request.get(Url, (Error, res, body) => {
  if (Error) console.log(Error);
  else {
    Read.writeFile(process.argv[3], body, 'utf8', (Error) => {
      if (Error) console.log(Error);
    });
  }
});
