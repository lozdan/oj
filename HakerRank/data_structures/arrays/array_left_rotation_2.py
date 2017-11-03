# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Arrays: Left Rotation
# problem url: https://www.hackerrank.com/challenges/array-left-rotation/problem
# date: 8/18/2017

n_d = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]

count = 0
for i in range(n_d[0]-n_d[1]):
    a = arr.pop(i+n_d[1])
    arr.insert(i,a)
print(*arr)