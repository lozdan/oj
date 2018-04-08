# author: Daniel Lozano
# source: CodeWars ( http://www.codewars.com )
# problem name: Kata > Sum of Triangular Numbers
# problem url: https://www.codewars.com/kata/580878d5d27b84b64c000b51

def sum_triangular_numbers(n):
    add = 0
    array = []
    for i in range(n):
        add += i + 1
        array.append(add)
    return sum(array)
