#!/usr/bin/node
exports.addMeMaybe = function (n, theFunction) {
  n = n + 1;
  theFunction(n);
};
