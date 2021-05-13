#!/usr/bin/node
let Arg = parseInt(process.argv[2], 10);
if (Arg) {
  while (Arg--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
