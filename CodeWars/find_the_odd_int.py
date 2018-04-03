# author: Daniel Lozano
# source: CodeWars ( http://www.codewars.com )
# problem name: Kata > Find the odd int
# problem url: http://www.codewars.com/kata/find-the-odd-int/

def find_it(seq):
    check = {}
    for num in seq:
        if num not in check:
            check[num] = 1
        else:
            check[num] += 1
    
    for numbers in check:
        if check[numbers] & 1 == 1:
            return numbers
