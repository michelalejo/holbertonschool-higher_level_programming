#!/usr/bin/node
const av = process.argv.slice(2);
if (av.length < 2) {
  console.log('0');
} else {
  av.sort((a, b) => {
    return (b - a);
  });
  console.log(av[1]);
}
