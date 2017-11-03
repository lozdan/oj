# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Arrays: Arrays - DS
# problem url: https://www.hackerrank.com/challenges/arrays-ds/problem
# date: 8/16/2017

n = int(input())
array = [int(i) for i in input().split()]

print(*(array[::-1]))