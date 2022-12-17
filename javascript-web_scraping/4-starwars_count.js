#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;
request(url, function (error, response, body) {
  let results = [];
  let count = 0;
  if (error) {
    console.log(error);
  } else {
    results = JSON.parse(body).results;
    for (const dict of results) {
      for (const item of dict.characters) {
        if (item.endsWith('/18/')) {
	  count++;
	}
	
      }

    }
    console.log(count);
  }
});
