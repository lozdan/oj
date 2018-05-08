# author: Daniel Lozano
# source: CodeWars ( http://www.codewars.com )
# problem name: Kata > Odd or Even?
# problem url: https://www.codewars.com/kata/odd-or-even/

def oddOrEven(arr):
    if sum(arr) & 1 == 1:
        return "odd"
    return "even"