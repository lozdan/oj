# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > primeCount
# problem url: https://codefights.com/challenge/WLCubrLrQ9grg7S8x

def primeCount(N):
    if N == 1:
        return 0
    numbers = [0] * N
    numbers[0], numbers[1] = 1, 1
    total = 2
    count = 0
    while count ** 2 < N:
        if numbers[count] == 0:
            for i in range(count * count, N, count):
                if numbers[i] == 0:
                    numbers[i] = 1
                    total += 1
        count += 1
    
    return N - total
            