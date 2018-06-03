/*
author: Daniel Lozano
source: CodeWars ( http://www.codewars.com )
problem name: Kata > Rock Off!
problem url: https://www.codewars.com/kata/rock-off/
*/

function solve(a, b) {
    let alice = 0;
    let bob = 0;

    for (let i = 0; i < 3; i++) {
        if (a[i] > b[i])
            alice++;
        else if (a[i] < b[i])
            bob++;
    }

    if (alice === bob)
        return alice + ', ' + bob + ': that looks like a "draw"! Rock on!'
    else if (alice > bob)
        return alice + ', ' + bob + ': Alice made "Kurt" proud!';
    else
        return alice + ', ' + bob + ': Bob made "Jeff" proud!';

}