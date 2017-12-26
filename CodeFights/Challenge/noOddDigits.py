# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > noOddDigits
# problem url: https://codefights.com/challenge/2pvFN4i8T64bF5F5a

def noOddDigits(n):
    n = str(n)
    output = ""
    for i in range(len(n)):
        if int(n[i]) % 2 == 0:
            output = output + n[i]
    if output:
        return int(output)
    return 0