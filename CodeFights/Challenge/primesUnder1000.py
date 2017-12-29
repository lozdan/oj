# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > primesUnder1000
# problem url: https://codefights.com/challenge/3zzNDGzENhxgeApTp

def primesUnder1000():
    multiplos = set()
    answer = ""
    for i in range(2, 1001):
        if i not in multiplos:
            answer = answer + "," + str(i)
            multiplos.update(range(i*i, 1001, i))
    return answer[1:]
