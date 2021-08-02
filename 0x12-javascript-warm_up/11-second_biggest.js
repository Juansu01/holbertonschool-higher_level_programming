#!/usr/bin/node

let biggest = 0;
let secondBiggest = 0;

if (process.argv.length === 2) {
  console.log('0');
} else if (process.argv.length === 3) {
  console.log('0');
} else {
  for (let i = 2; i < process.argv.length; i++) {
    if (process.argv[i] > biggest) {
      secondBiggest = biggest;
      biggest = process.argv[i];
    } else {
      continue;
    }
  }
  console.log(secondBiggest);
}
