#!/usr/bin/node
const Var = parseInt(process.argv[2], 10);
if (Var) {
  console.log('My number: ' + Var);
} else {
  console.log('Not a number');
}
