#!/usr/bin/node

const https = require('request');
const webPage = process.argv;

https.get(webPage[2], function (err, res) {
  if (err) {
    console.error(err);
  }
  console.log('code: ' + res.statusCode);
});
