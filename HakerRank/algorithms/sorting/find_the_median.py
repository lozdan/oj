# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Sorting: Find the Median
# problem url: https://www.hackerrank.com/challenges/find-the-median/problem
# date: 8/20/2017

n = int(input())
arr = [int(i) for i in input().split()]

count = [0 for i in range(max(arr)+1)]

for x in arr:
    count[x] += 1

output = []
for i in range(len(count)):
    if count[i] == 1:
        output.append(i)
    elif count[i] > 1:
        for j in range(count[i]):
            output.append(i)

print(output[n//2])