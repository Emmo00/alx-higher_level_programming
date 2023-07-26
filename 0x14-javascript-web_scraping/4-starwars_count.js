#!/usr/bin/node
const request = require('request');
const apiURL = process.argv[2];
request(apiURL, {}, (err, res, body) => {
  if (err) console.log(err);
  body = JSON.parse(body);
  const results = body.results;
  console.log(
    results.filter((movie) => {
      return movie.characters.some((character) => {
        return character.endsWith('/18/');
      });
    }).length
  );
});
