# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Sorting: Counting Sort 1
# problem url: https://www.hackerrank.com/challenges/countingsort1/problem
# date: 8/20/2017

n = int(input())
array = [int(i) for i in input().split()]

count = [0 for i in range(max(array)+1)]
for x in array:
    count[x] +=1

print(*count) 