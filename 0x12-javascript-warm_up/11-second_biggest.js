#!/usr/bin/node
/* script that searches the second biggest integer in the list of arguments */

const list = process.argv.slice(2).map(Number);
let bignum = 0;
if (list.length < 2) {
  console.log('0');
} else {
  list.sort((a, b) => a - b);
  bignum = list[list.length - 2];
  console.log(bignum);
}
