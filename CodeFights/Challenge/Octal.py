# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > Octal
# problem url: https://codefights.com/challenge/WLCubrLrQ9grg7S8x

def Octal(n):
    return sum(map(int, oct(n)[2:]))
