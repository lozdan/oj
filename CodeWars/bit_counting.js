/*
author: Daniel Lozano
source: CodeWars ( http://www.codewars.com )
problem name: Kata > Bit Counting
problem url: http://www.codewars.com/kata/bit-counting/
*/

var countBits = function(n) {
  var count = 0;
  while (n > 0){
    if (n & 1 === 1) count++;
    n = n >> 1;
  }
  
  return count;
};

