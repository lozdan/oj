# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > rangeDigitSum
# problem url: https://codefights.com/challenge/KJW7qMKX2ee375mPQ

def rangeDigitSum(A, B):
    total = 0
    for i in range(A, B + 1):
        total += digits_sum(i)
    return total
        
def digits_sum(value):
    res = 0
    while value != 0:
            res += value % 10
            value = value // 10
    return res
