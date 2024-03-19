#!/usr/bin/node
/* prints two arguments in format of "is" btw args eg. c[a1] is[constant] cool[a2] */

const a1 = process.argv[2];
const a2 = process.argv[3];

console.log(a1 + ' ' + 'is' + ' ' + a2);
