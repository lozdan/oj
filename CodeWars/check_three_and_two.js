/*
author: Daniel Lozano
source: CodeWars ( http://www.codewars.com )
problem name: Kata > Check three and two
problem url: https://www.codewars.com/kata/check-three-and-two
*/

function checkThreeAndTwo(array) {
  var check = {a: 0, b: 0, c: 0};
  var rep3 = false, rep2 = false;
  for (var i = 0; i < array.length; i++){
    check[array[i]]++;
  }
  
  for (var key in check){
    if (check[key] === 2)
      rep2 = true;
    else if (check[key] === 3)
      rep3 = true
  }
  
  return (rep2 && rep3);
}

