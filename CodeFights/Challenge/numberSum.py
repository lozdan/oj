# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > numberSum
# problem url: https://codefights.com/challenge/dgQMjRmDfGES8Dnum

def numberSum(n):
    return sum(range(1, n + 1)) if n >= 0 else sum(range(1, n -1, -1))
