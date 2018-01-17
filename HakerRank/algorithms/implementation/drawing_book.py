# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Drawing Book
# problem url: https://www.hackerrank.com/challenges/drawing-book/problem

n = int(input())
p = int(input())

print(min(n // 2 - p // 2, p // 2))
