#!/usr/bin/node
/* prints argument availability status */
const numargs = process.argv.lenght;
if (numargs <= 2) {
  console.log('No argument');
} else if (numargs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
