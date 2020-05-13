#!/usr/bin/node
const request = require('request');
let n = 0;
request.get(process.argv[2], (error, resp, body) => {
  if (error) throw error;
  for (const film of JSON.parse(body).results) {
    for (const line of film.characters) {
      if (line.endsWith('18/')) {
        n++;
      }
    }
  }
  console.log(n);
});
