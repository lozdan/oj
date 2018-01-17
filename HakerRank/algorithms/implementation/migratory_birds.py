# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Migratory Birds
# problem url: https://www.hackerrank.com/challenges/migratory-birds/problem

n = int(input())
a = list(map(int, input().split()))

freq = [0] * 5
for i in range(n):
    freq[a[i] - 1] += 1

print(freq.index(max(freq)) + 1)
