# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > prefix_Sums
# problem url: https://codefights.com/challenge/5Afg8xaWHX9cQ2Q6f

def prefixSums(a):
    numbers = [a[0]]
    for i in range(1, len(a)):
        numbers.append(numbers[i - 1] + a[i])
    return numbers
