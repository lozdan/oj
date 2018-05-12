/*
author: Daniel Lozano
source: CodeWars ( http://www.codewars.com )
problem name: Kata > Sum of positive
problem url: https://www.codewars.com/kata/sum-of-positive
*/

function positiveSum(arr) {
  let count = 0;
  for (let i = 0; i < arr.length; i++){
    if (arr[i] > 0)
      count += arr[i];
  }
  return count;
}
