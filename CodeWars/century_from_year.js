/*
author: Daniel Lozano
source: CodeWars ( http://www.codewars.com )
problem name: Kata > Century From Year
problem url: https://www.codewars.com/kata/century-from-year
*/

function century(year) {
  if (year % 100 === 0)
    return Math.floor(year / 100)
  return Math.floor(year / 100) + 1
}
