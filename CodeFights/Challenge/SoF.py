# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > SoF
# problem url: https://codefights.com/challenge/RwhbRkRviseEBBmbY

def SoF(n):
    carry_sum = 0
    for i in range(1, n + 1):
        carry_sum = carry_sum + factorial(i)
    return carry_sum
    
def factorial(num):
    if num == 0 or num == 1:
        return 1
    carry = 2
    for i in range(3, num + 1):
        carry = carry * i
    return carry
