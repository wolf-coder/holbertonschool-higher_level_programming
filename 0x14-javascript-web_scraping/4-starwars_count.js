#!/usr/bin/node
/*
  Write a script that prints the number of movies where the character “Wedge Antilles” is present.
*/

const request = require('request');

request.get(process.argv[2], function (Error, response, body) {
  if (Error) {
    console.log(Error);
  }
  let Count = 0;
  const data = JSON.parse(body);
  for (let i = 0; data.results[i] !== undefined; i++) {
    if (data.results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      Count++;
    }
  }
  console.log(Count);
});
