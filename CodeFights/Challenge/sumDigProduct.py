# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > sumDigProduct
# problem url: https://codefights.com/challenge/T9BnF2smtmRdpgQw2

from functools import reduce

def sumDigProduct(L, k):
    L = list(map(int, L))
    best = 0
    for i in range(0, len(L), k):
        best = max(best, reduce(lambda a, b: a * b, L[i: i + k]))                
    return sum(map(int, str(best)))
