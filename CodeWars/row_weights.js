/*
author: Daniel Lozano
source: CodeWars ( http://www.codewars.com )
problem name: Kata > Row Weights
problem url: https://www.codewars.com/kata/row-weights/train/javascript
*/

function rowWeights(array) {
  let team1 = 0;
  let team2 = 0;

  array.forEach((current, index) => {
    let even = index & 1;
    if (even === 0)
      team1 += current;
    else
      team2 += current;
  })

  return [team1, team2];
};