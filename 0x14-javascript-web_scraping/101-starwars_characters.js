#!/usr/bin/node
/*
  Write a script that prints all characters of a Star Wars movie:
    *The first argument is the Movie ID - example: 3 = “Return of the Jedi”
    *Display one character name by line in the same order of the list “characters” in the /films/ response
    *You must use the Star wars API
    *You must use the module request
*/

const Url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const request = require('request');

request.get(Url, async (Error, res, body) => {
  if (Error) console.log(Error);
  else {
    for (const Character of JSON.parse(body).characters) {
      const name = await new Promise((resolve, reject) => {
        request.get(Character, (Error, res, body) => {
          if (Error) reject(Error);
          else resolve(JSON.parse(body).name);
        });
      });
      console.log(name);
    }
  }
});
