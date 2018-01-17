# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Divisible Sum Pairs
# problem url: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

n,k = list(map(int, input().split()))
arr = list(map(int, input().split()))

total = 0
for i in range(n):
    for j in range(i):
        if (arr[i] + arr[j]) % k == 0:
            total += 1

print(total)
