#!/usr/bin/node
const a = process.argv.sort(function (a, b) {
  return b - a;
});
if (!a[2] || !a[3]) {
  console.log(0);
}
console.log(a[3]);
