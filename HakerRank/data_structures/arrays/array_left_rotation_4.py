# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Arrays: Left Rotation
# problem url: https://www.hackerrank.com/challenges/array-left-rotation/problem
# date: 8/18/2017

n, d = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]

aux_array = []


for i in range(n):
    if d < n:
        aux_array.append(arr[d])
        d += 1
    else:
        d = 0
        aux_array.append(arr[d])
        d += 1


print(*aux_array)
