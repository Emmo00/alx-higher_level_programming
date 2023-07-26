#!/usr/bin/node
const request = require("request");
api_url = process.argv[2];
request(api_url, {}, (err, res, body) => {
  if (err) console.log(err);
  body = JSON.parse(body);
  const results = body["results"];
  console.log(
    results.filter((movie) => {
      return movie["characters"].some((character) => {
        character.endsWith("/18/");
      });
    }).length
  );
});
