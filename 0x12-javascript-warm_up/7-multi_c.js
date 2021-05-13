#!/usr/bin/node
const Arg = parseInt(process.argv[2], 10);
if (Arg) {
  for (let i = 0; i < Arg; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
