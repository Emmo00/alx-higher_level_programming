#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiURL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request.get(apiURL, (err, res, data) => {
  if (err) console.log(err);
  const characters = data.match(/\/people\/[0-9]+\//gi);
  for (const character of characters) {
    request.get(`https://swapi-api.alx-tools.com/api${character}`, (error, res, data) => {
      if (error) console.log(error);
      console.log(JSON.parse(data).name);
    })
  }
});
