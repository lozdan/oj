# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Implementation > Picking Numbers
# problem url: https://www.hackerrank.com/challenges/picking-numbers/problem

n = int(input())

numbers = sorted(list(map(int, input().split())))

total = 0

for i in range(n - 1):
    k = i + total
    while k < n and numbers[k] - numbers[i] <= 1:
        k += 1
    if k - i > total:
        total = k - i

print(total)
