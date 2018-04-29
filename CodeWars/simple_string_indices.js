/*
author: Daniel Lozano
source: CodeWars ( http://www.codewars.com )
problem name: Kata > Simple string indices
problem url: https://www.codewars.com/kata/simple-string-indices
*/

function solve(str,idx){
 let openCount = 0
 if (str[idx] !== '(')
   return -1;
 for (let i = (idx + 1); i < str.length; i++){
   if (str[i] === '(')
     openCount++;
   else if (str[i] === ')' && openCount > 0)
     openCount--;
   else if (str[i] === ')' && openCount === 0)
     return i;
 }
 return -1;
}
