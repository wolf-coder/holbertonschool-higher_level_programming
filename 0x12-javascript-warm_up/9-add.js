#!/usr/bin/node
const a = parseInt(process.argv[2], 10);
const b = parseInt(process.argv[3], 10);
if (a && b) {
  console.log(a + b);
} else {
  console.log(a && b);
}
