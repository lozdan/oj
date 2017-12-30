# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > zeros
# problem url: https://codefights.com/challenge/4ZTivuTy4hJ2Ef3b4

def zeros(n):
    n = bin(n)[2:]
    zeros = 0
    for i in range(len(n)):
        if n[i] == "0":
            zeros += 1
    return zeros