/*
author: Daniel Lozano
source: CodeWars ( http://www.codewars.com )
problem name: Kata > Reversed sequence
problem url: https://www.codewars.com/kata/reversed-sequence/
*/

const reverseSeq = n => {
  let array = [];
  for (let i = n; i > 0; i--){
    array.push(i)
  }
  return array;
};
