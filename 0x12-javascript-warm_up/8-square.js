#!/usr/bin/node

const n = parseInt(process.argv[2], 10);
let square = '';
let i = n;
let j = n;
if (isNaN(n)) {
  console.log('Missing number of occurrences');
} else {
  while (i > 0) {
    while (j > 0) {
      square += 'X';
      j--;
    }
    console.log(square);
    i--;
  }
}
