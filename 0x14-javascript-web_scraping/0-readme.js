#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], { encoding: 'utf-8' }, (err, data) => {
  if (err) console.log(err);
  else console.log(data);
});
