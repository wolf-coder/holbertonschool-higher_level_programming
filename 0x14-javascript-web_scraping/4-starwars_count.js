#!/usr/bin/node
/*
  Write a script that prints the number of movies where the character “Wedge Antilles” is present.
*/

const request = require('request');
request.get(process.argv[2], (err, res, body) => {
  if (err) console.log(err);
  else {
    const movies = JSON.parse(body).results;
    let count = 0;
    movies.forEach(movie => {
      movie.characters.forEach(character => {
        if (character.includes('people/18/')) { count++; }
      });
    });
    console.log(count);
  }
});
