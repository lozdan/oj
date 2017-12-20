# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Arrays: Arrays - DS
# problem url: https://www.hackerrank.com/challenges/arrays-ds/problem
# date: 8/16/2017

n = int(input())
array = [int(i) for i in input().split()]


for i in range(n//2):
    array[i], array[(n-1)-i] = array[(n-1)-i], array [i]
        
        
print(*array)