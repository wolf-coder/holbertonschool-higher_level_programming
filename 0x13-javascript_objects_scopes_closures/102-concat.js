#!/usr/bin/node
const fs = require('fs');
const A = process.argv[2];
const B = process.argv[3];
const C = process.argv[4];
const dataA = fs.readFileSync(A, { encoding: 'utf8', flag: 'r' });
const dataB = fs.readFileSync(B, { encoding: 'utf8', flag: 'r' });
fs.writeFileSync(C, dataA + dataB);
