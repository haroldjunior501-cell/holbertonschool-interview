#!/usr/bin/node
/**
 * Prints all Star Wars characters for a given movie ID.
 */
const request = require('request');

const filmUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(filmUrl, (error, response) => {
  if (error) {
    return;
  }
  const characters = JSON.parse(response.body).characters;
  printCharacter(characters, 0);
});

/**
 * Recursively fetch and print character names in order.
 * @param {string[]} characters - Character API URLs
 * @param {number} index - Current character index
 */
function printCharacter (characters, index) {
  request.get(characters[index], (error, response, body) => {
    if (error) {
      return;
    }
    console.log(JSON.parse(body).name);
    if (index < characters.length - 1) {
      printCharacter(characters, index + 1);
    }
  });
}
