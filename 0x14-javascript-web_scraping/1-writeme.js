#!/usr/bin/node
// script writes a string to a file

const fs = require('fs');
const filepath = process.argv[2];
const write_ = process.argv[3];

fs.writeFile(filepath, write_, 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});
