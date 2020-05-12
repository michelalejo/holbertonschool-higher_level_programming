#!/usr/bin/node
exports.esrever = function (list) {
  const tmp = [];
  let i = 0;
  let size = list.length;
  for (i = 0; i < list.length; i++, size--) {
    tmp[i] = list[size - 1];
  }
  return (tmp);
};
