#!/usr/bin/node
/* script prints first integer */

const fa1 = process.argv[2];
const fa2 = Number(fa1);

if (isNaN(fa2)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Math.floor(fa2));
}
