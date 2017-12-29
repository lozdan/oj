# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > primeCount
# problem url: https://codefights.com/challenge/WLCubrLrQ9grg7S8x

def primeCount(N):
    l = set()
    count = 0
    for i in range(2, N):
        if i not in l:
            count += 1
            l.update(range(i * i, N, i))
    return count
            