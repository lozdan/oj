# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Warmup: Staircase
# problem url: https://www.hackerrank.com/challenges/staircase/problem
# date: 7/10/2017

n = int(input())
for i in range(n):
    print(" " * (n-1-i) + '#' * (i+1))