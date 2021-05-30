#!/usr/bin/node
const Dict = require('./101-data').dict;
const Res = {};
for (const key in Dict) {
  if (!Res[Dict[key]]) {
    Res[Dict[key]] = [];
  }
  Res[Dict[key]].push(key);
}
console.log(Res);
