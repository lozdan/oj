# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Sorting: Quicksort 1 - Partition
# problem url: https://www.hackerrank.com/challenges/quicksort1/problem
# date: 8/20/2017

n = int(input())
array = [int(i) for i in input().split()]

p = array[0]
left = []
equal = [array[0]]
right = []

for i in range(1, n):
    if array[i] < p:
        left.append(array[i])
    elif array[i] >= p:
        right.append(array[i])

print(*(left + equal + right))