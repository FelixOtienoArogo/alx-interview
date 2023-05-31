#!/usr/bin/node

const request = require('request');
const args = process.argv[2];

request('https://swapi-api.alx-tools.com/api/films/' + args, (error, response, body) => {
  if (error) throw error;
  else {
    const characters = JSON.parse(body).characters;
    order(characters, 0);
  }
});

const order = (characters, x) => {
  if (x < characters.length) {
    request(characters[x], function (err, res, bod) {
      if (err) throw err;
      else {
        console.log(JSON.parse(bod).name);
        order(characters, x + 1);
      }
    });
  }
};
