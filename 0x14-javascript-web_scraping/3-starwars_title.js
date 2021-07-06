#!/usr/bin/node
/*
  Write a script that prints the title of a Star Wars movie where
  the episode number matches a given integer.
*/

const ID = process.argv[2];
const request = require('request');
const Url = 'https://swapi-api.hbtn.io/api/films/' + ID;
request.get(Url, function (Error, response, body) {
  if (Error) {
    console.log(Error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
