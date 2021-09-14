#!/usr/bin/node

const req = require('request');
const argum = process.argv;
const webPage = 'https://swapi-api.hbtn.io/api/films/' + argum[2];

req(webPage, function (err, res, body) {
  if (err) {
    console.error(err);
  }
  console.log(JSON.parse(body).title);
});
