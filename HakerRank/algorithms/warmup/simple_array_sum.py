# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Warmup: Simple Array Sum
# problem url: https://www.hackerrank.com/challenges/simple-array-sum/problem
# date: 7/10/2017

n = int(input())
line = input().split()
for i in range(n):
    line[i] = int(line[i])       
print(sum(line)) 