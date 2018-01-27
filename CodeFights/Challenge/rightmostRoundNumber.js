/*
author: Daniel Lozano
source: CodeFights ( https://codefights.com )
problem name: Challenge > rightmostRoundNumber
problem url: https://codefights.com/challenge/npgAxzzMjLxhaXwSM
*/

function rightmostRoundNumber(inputArray) {
    for (var i = inputArray.length - 1; i >= 0; i--){
        if (inputArray[i] % 10 === 0){
            return i; 
        }
    }
    return -1;
}
