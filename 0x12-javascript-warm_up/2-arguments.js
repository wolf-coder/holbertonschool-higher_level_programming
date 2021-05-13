#!/usr/bin/node
const Lenargv = process.argv.length;
switch (Lenargv) {
  case 2:
    console.log('No argument');
    break;
  case 3:
    console.log('Argument found');
    break;
  default:
    console.log('Arguments found');
}
