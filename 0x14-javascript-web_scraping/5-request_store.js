#!/usr/bin/node

const req = require('request');
const argum = process.argv;
const webPage = argum[2];
const fs = require('fs');

req(webPage, function (err, res, body) {
  if (err) {
    console.error(err);
  }
  fs.writeFile(argum[3], body, err => {
    if (err) {
      console.error(err);
    }
    // file written successfully
  });
});
