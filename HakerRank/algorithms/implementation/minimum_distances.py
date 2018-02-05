# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Implementation > Minimum Distances
# problem url: https://www.hackerrank.com/challenges/minimum-distances/problem

n = int(input())

a = list(map(int, input().split()))
min_distance = -1

for i in range(n):
    for j in range(i + 1, n):
        if a[i] == a[j] and (abs(i - j) < min_distance or min_distance == -1):
            min_distance = abs(i - j)

print(min_distance)
