# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > EasyAsCounting
# problem url: https://codefights.com/challenge/FW47ZBAixW8ehaXTr

def EasyAsCounting(N):
    carry = 0
    for num in range(N):
        if num % 3 == 0 or num % 5 == 0:
            carry = carry + num
    return carry
