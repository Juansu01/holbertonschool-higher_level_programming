#!/usr/bin/node

let counter = 0;

for (counter in process.argv) {
  counter++;
}

if (counter === 3 || counter > 3) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
