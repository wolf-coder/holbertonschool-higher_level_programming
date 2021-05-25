#!/usr/bin/node
const List = require('./100-data').list;

const NewList = List.map((elem, index) => elem * index);
console.log(List);
console.log(NewList);
