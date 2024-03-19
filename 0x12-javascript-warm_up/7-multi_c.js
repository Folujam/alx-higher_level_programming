#!/usr/bin/node
/* prints x times */

const ptyms = Number(process.argv[2]);
if (isNaN(ptyms)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < ptyms) {
    console.log('C is fun');
    i++;
  }
}
