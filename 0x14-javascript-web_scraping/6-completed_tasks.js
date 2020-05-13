#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, { json: true }, (err, res, body) => {
  if (err) { console.log(err); } else {
    const result = {};
    for (const data of body) {
      if (data.completed) {
        if (result[data.userId]) {
          result[data.userId] += 1;
        } else {
          result[data.userId] = 1;
        }
      }
    }
    console.log(result);
  }
});
