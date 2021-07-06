#!/usr/bin/node
/*
  Write a script that computes the number of tasks completed by user id.
*/

const request = require('request');
request.get(process.argv[2], (Error, res, body) => {
  if (Error) console.log(Error);
  else {
    const TODO = JSON.parse(body);
    const ReadenNumber = {};
    TODO.forEach(Job => {
      if (Job.completed) {
        if (!ReadenNumber[Job.userId]) ReadenNumber[Job.userId] = 1;
        else ReadenNumber[Job.userId] += 1;
      }
    });
    console.log(ReadenNumber);
  }
});
