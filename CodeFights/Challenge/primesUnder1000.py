# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > primesUnder1000
# problem url: https://codefights.com/challenge/3zzNDGzENhxgeApTp

def primesUnder1000():
    multiples = set()
    answer = ""
    for i in range(2, 1001):
        if i not in multiples:
            answer = answer + "," + str(i)
            multiples.update(range(i*i, 1001, i))
    return answer[1:]
