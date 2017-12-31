# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > RemoveAdjacentLetters
# problem url: https://codefights.com/challenge/W9YFqP9Z3pE8vYhgh

def RemoveAdjacentLetters(N):
    result = N[0]
    for c in N:
        if c != result[-1]:
            result += c
    return result
