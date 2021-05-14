#!/usr/bin/node
// let L = '';
// let A = L + 'X';
// console.log(A)

const Arg = parseInt(process.argv[2], 10);
if (Arg) {
  let Line = '';
  for (let i = 0; i < Arg; i++) {
    Line = '';
    for (let j = 0; j < Arg; j++) {
      Line = Line + 'X';
    }
    console.log(Line);
  }
} else {
  console.log('Missing size');
}
