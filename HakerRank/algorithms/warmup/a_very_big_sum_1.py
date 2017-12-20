# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Warmup: A Very Big Sum
# problem url: https://www.hackerrank.com/challenges/a-very-big-sum/problem
# date: 7/10/2017

n = int(input())
list = input().split()
for i in range(n):
    list[i] = int(list[i])

for i in range(n-1):
    list [i+1] = list[i] + list[i + 1]
print(list[-1])
