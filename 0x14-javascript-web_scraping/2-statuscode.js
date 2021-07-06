#!/usr/bin/node
/*
  Write a script that display the status code of a GET request.
*/
const request = require('request');
request
  .get(process.argv[2])
  .on('response', function (Response) {
    console.log('code: ' + Response.statusCode);
  });
