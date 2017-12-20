# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Arrays: Left Rotation
# problem url: https://www.hackerrank.com/challenges/array-left-rotation/problem
# date: 8/18/2017

n, d = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]

print(*(arr[d:] + arr[:d]))
