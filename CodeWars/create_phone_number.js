/*
author: Daniel Lozano
source: CodeWars ( http://www.codewars.com )
problem name: Kata > Create Phone Number
problem url: https://www.codewars.com/kata/create-phone-number/train/javascript
*/

function createPhoneNumber(numbers){
  let phoneNumber = "(";
  
  numbers.forEach( (curr, ind) => {
    if (ind === 3)
      phoneNumber += ") ";
    else if (ind === 6)
      phoneNumber += "-";
    phoneNumber += curr;
  })
  
  return phoneNumber;
}