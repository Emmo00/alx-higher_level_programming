#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request.get(process.argv[2], {}, (err, res, data) => {
  if (err) console.log(err);
  fs.writeFile(process.argv[3], data, { encoding: 'utf-8' }, (err) => {
    if (err) console.log(err);
  });
});
