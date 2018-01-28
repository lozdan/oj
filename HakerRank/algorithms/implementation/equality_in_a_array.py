# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Implementation > Equalize the Array
# problem url: https://www.hackerrank.com/challenges/equality-in-a-array/problem

n = int (input())

numbers = list(map(int, input().split()))
check = [0] * max(numbers)

for c in numbers:
    check[c - 1] += 1

print(n - max(check))
