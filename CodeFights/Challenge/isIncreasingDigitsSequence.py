# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > isPangram
# problem url: https://codefights.com/challenge/JbpJhJYDovKY5TeqK

def isIncreasingDigitsSequence(n):
    while n >= 10:
        if (n // 10) % 10 >= n % 10:
            return False
        n = n // 10
    return True

