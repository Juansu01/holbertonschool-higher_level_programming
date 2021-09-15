#!/usr/bin/node

const req = require('request');
const argum = process.argv;
const myUrl = 'https://swapi-api.hbtn.io/api/films/' + argum[2];

req(myUrl, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const myChars = JSON.parse(body).characters;
  myFunction(myChars, 0);
});

function myFunction (array, index) {
  req(array[index], function (erro, response, body) {
    console.log(JSON.parse(body).name);
    if (index + 1 < array.length) {
      myFunction(array, index + 1);
    }
  });
}
