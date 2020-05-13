#!/usr/bin/node
const fs = require('fs');
const av = process.argv.slice(2);
const path = av[0];
const data = av[1];
fs.writeFile(path, data, 'utf8', (err) => {
  if (err) { console.log(err); }
});
