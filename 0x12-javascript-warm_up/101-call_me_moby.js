#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  let j = x;
  while (j--) {
    theFunction();
  }
};
