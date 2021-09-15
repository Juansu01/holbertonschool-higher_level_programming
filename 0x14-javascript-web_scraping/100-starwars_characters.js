#!/usr/bin/node

const req = require('request');
const argum = process.argv;
const myUrl = 'https://swapi-api.hbtn.io/api/films/' + argum[2];

req(myUrl, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const myChars = JSON.parse(body).characters;
  myChars.forEach((element) => {
    req(element, function (erro, resu, bodya) {
      console.log(JSON.parse(bodya).name);
    });
  });
});
