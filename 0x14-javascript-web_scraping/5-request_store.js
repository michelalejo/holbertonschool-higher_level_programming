#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const av = process.argv.slice(2);
const url = av[0];
const path = av[1];
request.get(url, (err, resp, body) => {
  if (err) throw err;
  fs.writeFile(path, body, 'utf8', (error) => {
    if (error) throw error;
  });
});
