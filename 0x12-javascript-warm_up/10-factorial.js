#!/usr/bin/node

const Arg = parseInt(process.argv[2], 10);
function recursive (n) {
  if (n === 1 || n === 0) {
    return 1;
  }
  return n * recursive(n - 1);
}
if (!Arg) {
  console.log(Arg && 1);
} else {
  console.log(recursive(Arg));
}
