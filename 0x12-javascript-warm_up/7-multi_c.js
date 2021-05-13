#!/usr/bin/node
let Arg2 = parseInt(process.argv[2], 10);
if (Arg2) {
  while (Arg2--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
