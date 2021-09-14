#!/usr/bin/node

const https = require('https');
const webPage = process.argv;

https.get(webPage[2], function (res) {
  console.log('code: ' + res.statusCode);
});
