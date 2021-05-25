#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let idx = list.indexOf(searchElement);
  let nb = 0;
  while (idx !== -1) {
    nb++;
    idx = list.indexOf(searchElement, ++idx);
  }
  return nb;
};
