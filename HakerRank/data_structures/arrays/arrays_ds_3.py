# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Arrays: Arrays - DS
# problem url: https://www.hackerrank.com/challenges/arrays-ds/problem
# date: 8/16/2017

n = int(input())
array = [int(i) for i in input().split()]

arr = []
count = n-1
while count >= 0:
    arr.append(array[count])
    count -= 1

print(*arr)