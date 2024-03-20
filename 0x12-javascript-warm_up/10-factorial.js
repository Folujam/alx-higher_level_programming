#!/usr/bin/node
/* script computes and prints a factorial */

const n = Number(process.argv[2]);
function factorial(n) {
    if (n <= 1 || isNaN(n)) {
        return (1);
    } else {
        return (n * (n - 1));
    }
}
console.log(factorial(n));
