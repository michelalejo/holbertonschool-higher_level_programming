#!/usr/bin/node
const string = ['C is fun'];
let i = 0;
const n = parseInt(process.argv[2], 10);
while (i < n && !(isNaN(n))) {
  console.log(string);
  i++;
}
if (isNaN(n)) {
  console.log('Missing number of occurrences');
}
