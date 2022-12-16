#!/usr/bin/node
const fs = require('fs');
const [, , file, text] = process.argv;

fs.writeFile(file, text, (err) => {
  if (err) console.error(err);
});
