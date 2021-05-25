#!/usr/bin/node

exports.esrever = function (list) {
  const ListRev = [];
  for (let idx = list.length - 1; idx >= 0; idx--) {
    ListRev.push(list[idx]);
  }
  return ListRev;
};
