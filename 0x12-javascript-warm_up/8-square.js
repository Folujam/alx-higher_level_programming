#!/usr/bin/node
/* prints a sqr of size x */

const sqsi = Number(process.argv[2]);
if (isNaN(sqsi)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < sqsi) {
    console.log('X'.repeat(sqsi));
    i++;
  }
}
