#!/usr/bin/node
/*
let biggest = 0;
let secondBiggest = 0;

if (process.argv.length === 2) {
  console.log('0');
} else if (process.argv.length === 3) {
  console.log('0');
} else {
  for (let i = 2; i < process.argv.length; i++) {
    if (process.argv[i] >= biggest) {
      secondBiggest = biggest;
      biggest = process.argv[i];
    } else if (process.argv[i] > secondBiggest){
      secondBiggest = process.argv[i];
    }
  }
  console.log(secondBiggest);
}
*/

if (process.argv.length === 2) {
  console.log('0');
} else if (process.argv.length === 3) {
  console.log('0');
} else {
  const myArr = process.argv;
  myArr.shift();
  myArr.shift();
  myArr.sort(function (a, b) {
    return a - b;
  });
  console.log(myArr[myArr.length - 2]);
}
