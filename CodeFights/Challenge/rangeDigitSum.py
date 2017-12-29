# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > rangeDigitSum
# problem url: https://codefights.com/challenge/KJW7qMKX2ee375mPQ

def rangeDigitSum(A, B):
    z = 0
    for i in range(A, B + 1):
        for j in range(len(str(i))):
            z = z + int(str(i)[j])
    return z
