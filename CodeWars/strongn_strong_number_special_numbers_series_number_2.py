# author: Daniel Lozano
# source: CodeWars ( http://www.codewars.com )
# problem name: Kata > STRONGN Strong Number (Special_Numbers_Series #2)
# problem url: https://www.codewars.com/kata/strongn-strong-number-special-numbers-series-number-2

def strong_num(number):
    temp = number
    total = 0
    while temp:
        total += factorial(temp % 10)
        temp = temp // 10
    if number == total:
        return "STRONG!!!!"
    else:
        return "Not Strong !!"


def factorial(num):
    total = 1
    for i in range(num, 1, -1):
        total *= i
    return total

