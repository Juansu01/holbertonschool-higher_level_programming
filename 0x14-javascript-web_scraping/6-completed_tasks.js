#!/usr/bin/node

const req = require('request');
const argum = process.argv;
const webPage = argum[2];

req(webPage, function (err, res, body) {
  if (err) {
    console.error(err);
  }
  const tasksDict = {};
  const myDict = (JSON.parse(body));

  for (const task in myDict) {
    const currentTask = myDict[task];
    const currentId = myDict[task].userId;

    if (currentTask.completed) {
      if (tasksDict[currentId] === undefined) {
        tasksDict[currentId] = 1;
      } else {
        tasksDict[currentId]++;
      }
    }
  }
  console.log(tasksDict);
});
