#!/usr/bin/node

const a = parseInt(process.argv[2]);

function factorialize (num) {
  if (num === 1) {
    return 1;
  } else {
    return (num * factorialize(num - 1));
  }
}

if (isNaN(parseInt(process.argv[2]))) {
  console.log('1');
} else {
  console.log(factorialize(a));
}
