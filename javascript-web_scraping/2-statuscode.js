#!/usr/bin/node
require('request').get(process.argv[2], function (err, r) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + r.statusCode);
  }
});
