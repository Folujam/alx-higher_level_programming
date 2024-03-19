#!/usr/bin/node
/* script prints first argument */

const argsarr = process.argv;

if (argsarr[2] === undefined) {
  console.log('No arguments');
} else {
  console.log(argsarr[2]);
}
