#!/usr/bin/node

const argv = require('process').argv;
const fs = require('fs');
const file = argv[2];

fs.readFile(file, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
