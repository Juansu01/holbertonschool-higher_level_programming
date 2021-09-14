#!/usr/bin/node

const req = require('request');
const argum = process.argv;
const webPage = argum[2];
let x = 0;

req(webPage, function (err, res, body) {
  if (err) {
    console.error(err);
  }
  const myResult = JSON.parse(body).results;
  for (const movie of myResult) {
    for (const actor of movie.characters) {
      if (actor.includes('18')) {
        x++;
      }
    }
  }
  console.log(x);
});
