# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Sock Merchant
# problem url: https://www.hackerrank.com/challenges/sock-merchant/problem

n = int(input())
a = sorted(list(map(int, input().split())))

total = 0
index = 1
while index < n:
    if a[index] == a[index - 1]:
        total += 1
        index += 2
    else:
        index += 1

print( total)
