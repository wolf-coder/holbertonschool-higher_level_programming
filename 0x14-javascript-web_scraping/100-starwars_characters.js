#!/usr/bin/node
/*
  Write a script that prints all characters of a Star Wars movie:
*/

const Url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const request = require('request');
request.get(Url, (Error, res, body) => {
  if (Error) console.log(Error);
  else {
    JSON.parse(body).characters.forEach(Char => {
      request.get(Char, (Error, res, body) => {
        if (Error) console.log(Error);
        else console.log(JSON.parse(body).name);
      });
    });
  }
});
