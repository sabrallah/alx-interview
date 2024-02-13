#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body);

    films.results.forEach((film) => {
      console.log(`Characters in ${film.title}:`);
      
      film.characters.forEach((characterUrl) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            console.error(error);
          } else {
            const character = JSON.parse(body);
            console.log(character.name);
          }
        });
      });
      console.log("\n");
    });
  }
});
