#!/usr/bin/node

const fs = require('fs');
const fileName = process.argv;

fs.readFile(fileName[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
